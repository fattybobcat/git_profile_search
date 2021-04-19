# Git_profile_search

[![git_pull_request](https://github.com/fattybobcat/Git_profile_search/actions/workflows/main.yml/badge.svg)](https://github.com/fattybobcat/Git_profile_search/actions/workflows/main.yml)

## Описание

Проект позволяет производить поиск Pull-Request определенного users.
При поиске, если user существует, будет предоставлена информация о Pull-Request данного user.
На каждой странице будет выведено до 100 записей последний Pull-Request, рассортированных по проектам.
У каждого проекта показано: 
| №  | Name Project | Project Link | Star Project | Merged Pull-Request Link | Numbers of Сomments  | SNot Merged Pull-Request Link | Numbers of Сomments |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |  ------------- |

## Инициализация

* Клонируйте репозиторий с проектом https://github.com/fattybobcat/Git_profile_search.git
* Создайте виртуальное пространство `python -m venv venv` и активируйте его.
* Установите необходимые модули `pip install -r requirements.txt`

Если нужно выполнять большое количество запросов, то необходимо создать .venv файл с вашим именем на HitHub и токеном
```
USERNAME_GITHUB= # your Username
TOKEN_GITHUB= # your Token
```

* Запустите приложение `python manage.py runserver`

## Работа с проектом

Откройте в браузере ссылку: http://127.0.0.1:8000/ и можете начинать поиск Pull-Request необходимого вам users

## Aвтор проекта

Петрук Александр - [GitHub](https://github.com/fattybobcat)

[резюме](https://github.com/fattybobcat/Git_profile_search/blob/main/%D0%9F%D0%B5%D1%82%D1%80%D1%83%D0%BA_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_PythonDeveloper.pdf)

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)
