import string

from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for movie in movies:
        if preprocess_text(query) in preprocess_text(movie["title"]):
            results.append(movie)
            if len(results) >= limit:
                break
    return results


def preprocess_text(text: str) -> str:
    text_lower = text.lower()
    text_remove = text_lower.translate(str.maketrans("", "", string.punctuation))
    return text_remove
