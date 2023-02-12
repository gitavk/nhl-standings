import asyncio
from typing import Optional

import aiohttp


async def page(url: str) -> Optional[str]:
    # Для повторяющихся запросов рекомендуется переиспользовать одну сессию aiohttp.ClientSession
    # Подробнее: https://docs.aiohttp.org/en/stable/client_quickstart.html
    # Но это бы усложнило пример
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


# Чтобы понять, что здесь происходит, вы можете ознакомиться с документацией asyncio:
# https://docs.python.org/3/library/asyncio.html
async def multiple_pages(urls: list[str]) -> Optional[list[str]]:
    # Конкурентно вызываем page() для каждой входящей ссылки
    handles = list(map(lambda x: asyncio.create_task(page(x)), urls))

    pages = []
    # Получаем результаты в список
    for handle in handles:
        pages.append(await handle)

    return pages
