# Визуализация для [парсера](https://github.com/Stranix/parser_library).

Сайт, визуализирующий результат работы [парсера](https://github.com/Stranix/parser_library).  
*Для работы требуется: `python >= 3.10`*

Пример результат:  
![screenshot site](https://github.com/Stranix/library_site/blob/master/site_example.jpg?raw=true)

## Как использовать
- Клонируем репозиторий
```shell
git clone https://github.com/Stranix/library_site.git
```
- Устанавливаем зависимости
```shell
pip install -r requirements.txt
```
- Рендерим страницы и запускаем локальный веб сайт
```shell
python3 render_website.py
```
Локальный сайт доступен по адресу: [http://127.0.0.1:5500/](http://127.0.0.1:5500/)  

## Аргументы `render_website.py`
- `--books_per_page`, `-bpp` -- Количество книг на страницу сайта. По умолчанию ровно `20` книг.
- `--template`, `-t`, - Полный путь до базового шаблона. По умолчанию `templates/template.html`.
- `--books`, `-b` - Путь до базового шаблона. По умолчанию `downloaded_books_info.json`.  

Пример:
```shell
python3 render_website.py --books_per_page 10
```
- Создаем страницу в репозитории используя GitHub Pages.  
Как это сделать можно прочитать в официальной документации [здесь](https://docs.github.com/ru/pages)  
- Смотрим сайт  
Пример сайта доступен по [ссылке](https://stranix.github.io/library_site/pages/index1.html).

Сгенерированный сайт можно открывать локально, так же выкладывать на любой другой хостинг.

## Формат `downloaded_books_info.json`
```json
[
  {
        "title": "Алиби",
        "author": "ИВАНОВ Сергей",
        "genres": [
            "Научная фантастика",
            "Прочие Детективы"
        ],
        "book_saved_path": "media/books/239_Алиби.txt",
        "poster_saved_path": "media/images/239.jpg"
    }
]
```

*`JSON` и `media` файлы можно получить воспользовавшись парсером по [ссылке](https://github.com/Stranix/parser_library)*

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).