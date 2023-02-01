import os
import requests
from src.tools import generate_pdf, sort_pic


class Crawler:
    textbooks: dict[str, dict[str, int]]

    def __init__(self, textbooks: dict[str, dict[str, int]]) -> None:
        self.textbooks = textbooks

    def download_pic(self, book: str) -> None:
        '''
        description: 下载图片
        param       {*} self
        param       {str} book
        return      {*}
        author     : Senkita
        '''
        os.makedirs(book, exist_ok=True)
        book_id: int = self.textbooks[book]['id']
        pages: int = self.textbooks[book]['pages']
        for page in range(pages):
            page_num: int = page + 1

            url: str = 'https://book.pep.com.cn/{}/files/mobile/{}.jpg'.format(
                book_id, page_num)
            res = requests.get(url)

            with open('{}/{}.jpg'.format(book, page_num), 'wb') as f:
                f.write(res.content)

    def run(self) -> None:
        for book in self.textbooks:
            self.download_pic(book)
            files: list = sort_pic(book)
            generate_pdf(book, files)
