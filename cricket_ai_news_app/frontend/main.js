const form = document.getElementById("search-form");
const queryInput = document.getElementById("query");
const pageSizeSelect = document.getElementById("page-size");
const statusEl = document.getElementById("status");
const summaryEl = document.getElementById("summary");
const articlesEl = document.getElementById("articles");
const button = document.getElementById("search-button");
const buttonText = document.getElementById("search-button-text");
const spinner = document.getElementById("search-spinner");

function setLoading(loading, message) {
  if (loading) {
    button.disabled = true;
    spinner.hidden = false;
    buttonText.textContent = "Fetching news…";
  } else {
    button.disabled = false;
    spinner.hidden = true;
    buttonText.textContent = "Get AI summary";
  }
  statusEl.textContent = message || "";
  statusEl.classList.remove("error");
}

function setError(message) {
  statusEl.textContent = message;
  statusEl.classList.add("error");
}

function renderSummary(text) {
  summaryEl.innerHTML = "";
  if (!text) {
    const p = document.createElement("p");
    p.className = "placeholder";
    p.textContent =
      "No summary available. Try another search phrase like “World Cup” or “PSL”.";
    summaryEl.appendChild(p);
    return;
  }
  const pre = document.createElement("div");
  pre.className = "summary-content";
  pre.textContent = text;
  summaryEl.appendChild(pre);
}

function renderArticles(articles) {
  articlesEl.innerHTML = "";
  if (!articles || articles.length === 0) {
    const p = document.createElement("p");
    p.className = "placeholder";
    p.textContent = "No matching cricket articles found.";
    articlesEl.appendChild(p);
    return;
  }

  for (const article of articles) {
    const wrapper = document.createElement("div");
    wrapper.className = "article";

    const thumb = document.createElement("div");
    thumb.className = "thumb";
    if (article.urlToImage) {
      thumb.style.backgroundImage = `url('${article.urlToImage}')`;
    } else {
      thumb.style.backgroundImage =
        "radial-gradient(circle at 30% 20%, #22c55e, #0f172a 52%)";
    }

    const body = document.createElement("div");
    body.className = "article-body";

    const titleEl = document.createElement("h3");
    titleEl.className = "article-title";
    const link = document.createElement("a");
    link.href = article.url || "#";
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.textContent = article.title || "Untitled article";
    titleEl.appendChild(link);

    const meta = document.createElement("div");
    meta.className = "article-meta";
    const parts = [];
    if (article.source) parts.push(article.source);
    if (article.publishedAt) {
      const date = new Date(article.publishedAt);
      if (!isNaN(date)) {
        parts.push(date.toLocaleString());
      }
    }
    meta.textContent = parts.join(" • ");

    const desc = document.createElement("p");
    desc.className = "article-desc";
    desc.textContent =
      article.description || "No description. Open the link for full details.";

    body.appendChild(titleEl);
    body.appendChild(meta);
    body.appendChild(desc);

    wrapper.appendChild(thumb);
    wrapper.appendChild(body);
    articlesEl.appendChild(wrapper);
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const topic = (queryInput.value || "").trim();
  const pageSize = pageSizeSelect.value || "10";

  const params = new URLSearchParams();
  if (topic) params.set("query", topic);
  params.set("page_size", pageSize);

  setLoading(true, "Talking to the cricket news API…");

  try {
    const response = await fetch(`/api/news?${params.toString()}`);
    if (!response.ok) {
      let message = `Request failed with status ${response.status}`;
      try {
        const data = await response.json();
        if (data && data.detail) {
          message = Array.isArray(data.detail)
            ? data.detail.map((d) => d.msg || d).join(", ")
            : data.detail;
        }
      } catch {
        // ignore JSON parse errors
      }
      throw new Error(message);
    }

    const result = await response.json();
    renderSummary(result.summary);
    renderArticles(result.articles);
    setLoading(false, `Loaded ${result.articles?.length || 0} articles.`);
  } catch (err) {
    console.error(err);
    setError(
      err && err.message
        ? err.message
        : "Something went wrong while fetching cricket news."
    );
    setLoading(false);
  }
});

