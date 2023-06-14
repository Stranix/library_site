import sys
import argparse
import more_itertools

from livereload import Server

import services


def create_arg_parser():
    description = 'Генерируем веб версию для парсера ' \
                  'https://github.com/Stranix/parser_library '
    epilog = """
    В качестве хостинга используем github pages
    """

    arg_parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog
    )

    arg_parser.add_argument('--books_per_page', '-bpp', default=20, metavar='', type=int,
                            help='''количество книг на страницу сайта (
                            пагинация). По умолчанию ровно 20 книг'''
                            )

    return arg_parser


def on_reload():
    """Генерируем страницы сайта с книгами.
    Генерация происходит при запуске скрипта или при включенном liveserver при
    изменении шаблона jinja
    """
    parser = create_arg_parser()
    args = parser.parse_args()

    books_per_page = args.books_per_page
    template = services.get_jinja_template('templates/template.html')

    chunked_books = list(
        more_itertools.chunked(
            services.get_books_from_json_file('downloaded_books_info.json'),
            books_per_page
        )
    )

    books_count = len(chunked_books)

    for page, books in enumerate(chunked_books, start=1):
        rendered_page = template.render(
            books=books,
            books_count=books_count,
            current_page=page
        )

        services.save_rendered_page(f'index{page}.html', rendered_page)


if __name__ == '__main__':
    try:
        on_reload()

        server = Server()
        server.watch('templates/template.html', on_reload)
        server.serve(root='.')

    except FileNotFoundError:
        error_msg = 'Для работы необходим файл с книгами {} в корне проекта'
        error_msg = error_msg.format('downloaded_books_info.json')
        print(error_msg)

        sys.exit()

    except KeyboardInterrupt:
        print('Завершение работы')
