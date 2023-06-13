import sys
import services
import more_itertools

from livereload import Server


def on_reload():
    """Генерируем страницы сайта с книгами.
    Генерация происходит при запуске скрипта или при включенном liveserver при
    изменении шаблона jinja
    """
    template = services.get_jinja_template('templates/template.html')

    books_chunked = list(
        more_itertools.chunked(
            services.get_books_from_json_file('downloaded_books_info.json'),
            20
        )
    )

    books_count = len(books_chunked)

    for page, books in enumerate(books_chunked, start=1):
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
        error_msg = 'Для работы необходим файл с книгами {} в корне проекта'.format(
                'downloaded_books_info.json'
        )
        print(error_msg)
        sys.exit()

    except KeyboardInterrupt:
        print('Завершение работы')
