import os
import json

from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape


def save_rendered_page(
        filename: str,
        rendered_page: str,
        folder: str = 'pages/'
):
    """Сохраняет сгенерированную страницу html на диск.

    :param filename: имя файла.
    :param rendered_page: строка с html для сохранения.
    :param folder: папка для сохранения.

    """

    os.makedirs(folder, exist_ok=True)

    path_to_save = os.path.join(folder, filename)

    with open(path_to_save, 'w', encoding='utf8') as file:
        file.write(rendered_page)


def get_books_from_json_file(filename: str) -> dict:
    """Получаем информацию о книгах из json файла.

    :param filename: имя файла.

    :return: словарь с информацией о книгах.
    """

    with open(filename, 'r', encoding='utf8') as json_file:
        books = json.load(json_file)

    return books


def get_jinja_template(filename: str) -> Template:
    """Получаем jinja Template.

    :param filename: имя файла шаблона.

    :return: jinja Template
    """

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template(filename)

    return template
