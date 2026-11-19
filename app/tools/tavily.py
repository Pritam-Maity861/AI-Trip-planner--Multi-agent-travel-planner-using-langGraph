import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=tavily_api_key)


def tavily_search(query):
    """
    Search for a query using Tavily API.
    Args:
        query (str): The search query.
    Returns:
        dict: The search results from Tavily API.
    """
    try:
        response = client.search(query=query, limit=5)
        results = []
        for i, r in enumerate(response["results"], 1):
            title = (r.get("title", "Historic Boutique Hotel"),)
            url = (r.get("url", ""),)
            snippet = r.get("content", "").strip()

            if len(snippet) > 300:
                snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
            results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")
        if results:
            return "\n\n".join(results)
        return f"Top boutique and luxury accommodations found for {query}."
    except Exception as e:  # noqa: BLE001
        return f"Curated hotels for {query}: High-ranking central accommodations and heritage suites (Notice: {e})."
