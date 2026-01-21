#!/usr/bin/env python3

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            data = load_data("data/movies.json")
            movies_results = []
            for movie in data["movies"]:
                if args.query.lower() in movie["title"].lower():
                    movies_results.append(movie)
            movie_sorted = sorted(movies_results, key=lambda x: x["id"])
            five_movies = movie_sorted[:5]
            for movie in five_movies:
                print(f"{movie['id']}. {movie['title']}")
        case _:
            parser.print_help()


def load_data(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    main()
