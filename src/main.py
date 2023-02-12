import asyncio
from typing import Optional

import extract
import load
import transform
import model

BEATPORT_URL = "https://www.beatport.com"


async def main():
    # Получаем главную страницу Beatport
    main_page: Optional[str] = await extract.page(BEATPORT_URL)

    # Достаём из неё ссылки на Top 100 страницы для каждого жанра
    genre_top_100_urls: list[str] = transform.main_page_to_genre_top_100_urls(main_page)

    # Конкурентно получаем содержимое Top 100 страниц для каждого жанра
    genre_top_100_pages: list[str] = await extract.multiple_pages(genre_top_100_urls)

    # Анализируем Top 100 страницы, составляя отчёты для каждого музыкального жанра
    genre_reports: list[model.Report] = transform.genre_top_100_pages_to_reports(
        genre_top_100_pages
    )

    # Отображаем наши отчёты в виде статической веб-страницы
    load.build(genre_reports)


if __name__ == "__main__":
    asyncio.run(main())
