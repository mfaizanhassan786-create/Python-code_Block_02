# Cricket AI News App

Full‑stack demo that fetches **cricket news** and generates an **AI summary**.

Backend is built with **FastAPI**, frontend is a simple HTML/CSS/JS page served from the same server.

---

## 1. Install Python packages

From the `cricket_ai_news_app` folder:

```bash
cd cricket_ai_news_app
pip install -r requirements.txt
```

On Windows PowerShell you can run:

```powershell
cd cricket_ai_news_app
pip install -r requirements.txt
```

---

## 2. Configure API keys

The backend expects:

- `NEWS_API_KEY` – from `https://newsapi.org` (free tier is enough)
- `OPENAI_API_KEY` – from your OpenAI account (for AI summaries)

You can set these as **environment variables** in PowerShell before running the server:

```powershell
$env:NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"
$env:OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"
```

Keep that PowerShell window open so the variables stay active.

If you don’t set `OPENAI_API_KEY`, the app will still work but will only show a simple list of top headlines instead of a rich AI summary.

---

## 3. Run the backend (serves the frontend too)

From inside `cricket_ai_news_app`:

```powershell
uvicorn backend.main:app --reload --port 8000
```

Then open this in your browser:

- `http://127.0.0.1:8000/`

The backend:

- `GET /api/news` – fetches cricket news + AI summary
- `/` – serves the main `index.html` page
- `/static/*` – serves the CSS and JS files

---

## 4. Using the app

1. Open `http://127.0.0.1:8000/` in your browser.
2. Type a **cricket topic** – e.g. `India`, `Babar Azam`, `IPL`, `Ashes`.
3. Choose how many articles to fetch.
4. Click **“Get AI summary”**.

The page will:

- Call the FastAPI backend.
- Fetch latest cricket articles from NewsAPI.
- Ask OpenAI to generate a short, friendly cricket summary.
- Show you both the AI summary and the list of source articles.

