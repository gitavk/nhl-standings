import os

from jinja2 import Environment, FileSystemLoader

import model

TEMPLATE_PATH = "templates"
INDEX_NAME = "index.html"
BUILD_PATH = "build"


# Чтобы понять, что здесь происходит, вы можете ознакомиться с Jinja Documentation:
# https://jinja.palletsprojects.com/
def build(reports: list[model.Report]):
    # Создаём папку для билда
    os.makedirs(BUILD_PATH, exist_ok=True)

    # Инициализируем движок шаблонов Jinja
    # Этот этап рекомендуется выполнять только один раз
    jinja = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

    # Рендерим содержимое
    content = jinja.get_template(INDEX_NAME).render(reports=reports)

    # Открываем файл на чтение
    with open(os.path.join(BUILD_PATH, INDEX_NAME), "w", encoding="utf-8") as f:
        # Заполняем файл содержимым
        f.write(content)
