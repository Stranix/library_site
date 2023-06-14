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
Количество книг на странице задается через параметр  `--books_per_page`. По Значение параметра ровно `20`.  
Пример:
```shell
python3 render_website.py --books_per_page 10
```
- Создаем страницу в репозитории используя GitHub Pages.  
Как это сделать можно прочитать в официальной документации [здесь](https://docs.github.com/ru/pages)  
- Смотрим сайт  
Пример сайта доступен по [ссылке](https://stranix.github.io/parser_library/pages/index1.html).

Сгенерированный сайт можно открывать локально, так же выкладывать на любой другой хостинг.


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).