import wikipedia


def wiki_summary(query: str):
  # summary = wikipedia.summary(query, sentences=3, auto_suggest=True)
  print(f"requested wiki search q: {query}")
  search_results = wikipedia.search(query)
  summaries = []
  for i in range(2):
    summary = fetch_formatted_page_summary(search_results[i])
    if summary is not None:
      summaries.append(summary)

  print(f"requested wiki search q: {query} returned: ")
  print("\n\n".join(summaries))

  return "\n\n".join(summaries)


def fetch_formatted_page_summary(page: str):
  try:
    wiki_page = wikipedia.page(title=page)
    return f"Page: {page}\nSummary: {wiki_page.summary}"
  except (
      wikipedia.exceptions.PageError,
      wikipedia.exceptions.DisambiguationError,
  ):
    return None


wiki_summary_description = """
  Useful for when you need to answer general questions about people, places, companies, historical events, or other subjects.Input should be a search query.
  """
