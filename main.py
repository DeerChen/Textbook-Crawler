import json5
from src.Crawler import Crawler
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        book, book_id, pages = sys.argv[1:4]

        textbooks: dict[str, dict[str, int]] = {
            book: {
                'id': int(book_id),
                'pages': int(pages)
            }
        }
    else:
        with open('textbooks.jsonc', 'r') as f:
            textbooks = json5.loads(f.read())  # type: ignore

    crawler = Crawler(textbooks)
    crawler.run()
