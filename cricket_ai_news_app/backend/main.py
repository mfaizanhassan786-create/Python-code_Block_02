import os
from typing import List, Optional

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

try:
    from openai import AsyncOpenAI
except ImportError:  # pragma: no cover - handled at runtime
    AsyncOpenAI = None  # type: ignore


NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


app = FastAPI(title="Cricket AI News API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


frontend_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)
if os.path.isdir(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


@app.get("/")
async def read_root() -> FileResponse:
    """
    Serve the main frontend page.
    """
    index_path = os.path.join(frontend_dir, "index.html")
    return FileResponse(index_path)


@app.get("/api/news")
async def get_cricket_news(
    query: str = Query("cricket", description="Search term, e.g. team or player name"),
    page_size: int = Query(10, ge=1, le=50),
) -> dict:
    """
    Fetch latest cricket-related news and return with an AI-generated summary.
    """
    if not NEWS_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="NEWS_API_KEY is not configured on the server.",
        )

    params = {
        "q": f"cricket {query}".strip(),
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY,
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        try:
            response = await client.get(NEWS_API_URL, params=params)
        except httpx.RequestError:
            raise HTTPException(
                status_code=502,
                detail="Failed to reach the news service.",
            )

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"News service error: {response.text}",
        )

    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        return {
            "summary": "No recent cricket news found for this query.",
            "articles": [],
        }

    summary = await summarize_articles_with_ai(articles)

    clean_articles: List[dict] = []
    for a in articles:
        clean_articles.append(
            {
                "title": a.get("title"),
                "description": a.get("description"),
                "url": a.get("url"),
                "publishedAt": a.get("publishedAt"),
                "source": (a.get("source") or {}).get("name"),
                "urlToImage": a.get("urlToImage"),
            }
        )

    return {
        "summary": summary,
        "articles": clean_articles,
    }


async def summarize_articles_with_ai(articles: List[dict]) -> str:
    """
    Use OpenAI (if available and configured) to summarize the list of articles.
    Falls back to a simple rule-based summary if OpenAI is not configured.
    """
    titles = [a.get("title") for a in articles if a.get("title")]
    descriptions = [a.get("description") for a in articles if a.get("description")]

    if not titles and not descriptions:
        return "Latest cricket updates are available, but article details are missing."

    # Fallback if OpenAI SDK or API key is not available
    if AsyncOpenAI is None or not OPENAI_API_KEY:
        top = titles[:3]
        if not top:
            return "Here are some recent cricket stories, but AI summarization is disabled."
        return "AI summarization is not configured. Top headlines:\n- " + "\n- ".join(
            top
        )

    client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    # Keep the prompt compact
    joined = "\n".join(
        f"- {t} :: {d}" for t, d in zip(titles[:10], descriptions[:10])
    )
    prompt = (
        "You are a cricket news analyst. Summarize these recent cricket stories in 3-5 short bullet points, "
        "highlighting major matches, players, and any controversies. Keep it simple and clear.\n\n"
        f"{joined}"
    )

    try:
        completion = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert cricket journalist."},
                {"role": "user", "content": prompt},
            ],
        )
    except Exception:
        top = titles[:3]
        if not top:
            return "Here are some recent cricket stories, but AI summarization failed."
        return "AI summarization failed. Top headlines:\n- " + "\n- ".join(top)

    content: Optional[str] = None
    try:
        content = completion.choices[0].message.content  # type: ignore[attr-defined]
    except Exception:
        pass

    if not content:
        top = titles[:3]
        if not top:
            return "Here are some recent cricket stories, but AI summarization failed."
        return "AI summarization failed. Top headlines:\n- " + "\n- ".join(top)

    return content.strip()


if __name__ == "__main__":  # pragma: no cover
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

