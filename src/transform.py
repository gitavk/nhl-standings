from typing import Optional

import model

# В данном модуле будет находиться код, специфичный для вашего приложения


def main_page_to_genre_top_100_urls(_page: str) -> Optional[list[str]]:
    raise NotImplementedError


def genre_top_100_pages_to_reports(_pages: list[str]) -> Optional[list[model.Report]]:
    raise NotImplementedError
