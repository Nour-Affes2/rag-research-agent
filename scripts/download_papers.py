import arxiv
import os
from time import sleep

OUT_DIR = "../data/pdfs"
os.makedirs(OUT_DIR, exist_ok=True)

def download_arxiv(query="retrieval augmented generation", max_results=30, sleep_s=1.0):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    for result in search.results():
        title_safe = "".join(c for c in result.title if c.isalnum() or c in (" ", "_", "-")).rstrip()
        filename = f"{result.entry_id.split('/')[-1]}__{title_safe[:80]}.pdf"
        path = os.path.join(OUT_DIR, filename)
        if not os.path.exists(path):
            try:
                print("Downloading:", result.title)
                result.download_pdf(filename=path)
                sleep(sleep_s)  # be kind to the server
            except Exception as e:
                print("Failed to download:", result.entry_id, e)
        else:
            print("Already exists:", filename)

if __name__ == "__main__":
    download_arxiv(query="retrieval augmented generation", max_results=25)
