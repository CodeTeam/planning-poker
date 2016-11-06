# Tornado starter project
Каркас для создания торнадо приложения.
В комплекте:
* Docker
* PostgreSQL
* Tornado
* Peewee ORM (async)
* Django migrations
* Tests (pytest)
* Python-Rico/Tornado (https://bitbucket.sberned.ru/projects/EV/repos/python_rico)
# Структура приложения
При построении приложения следует использовать модульную MV архитектуру. Отдельные элементы бизнес логики должны быть
реализованы в виде отдельных пакетов в папке application.
Каждый пакет может быть представлен следующей схемой:
* models.py - модели PeeWee для приложения (M)
* handlers.py - обработчики бизнес-логики (V)
* schemas.py - опциональные схемы для валидации данных
# Настройки
В текущей реализации для старта приложения требуется изменить (при необходимости) следующие настройки:
./docker-compose.yml - Параметры доступа к базе данных для разработки (контейнеры pg и api)
./application/settings.py - Параметры доступа к базе данных (DATABASE_URL default)
./migrations/settings.py - Параметры доступа к базе данных (DATABASE URL default)
./bin/build.sh, ./bun/run.sh - Имя контейнера
# Migrations
В текущей реализации для использования Django миграций требуется дублировать модели в файле migrations/model_app/models.py
Формат описания моделей - Django (https://docs.djangoproject.com/en/1.10/topics/db/models/)
Создание миграций: python migrations/manage.py makemigrations
Применение миграций: python migrations/manage.py migrate
Альтернативный способ создания моделей:
`
from application.module_name.models import ModelName
from application.base.models import db
with db.allow_sync():
    ModelName.create_table()
`
Этот код создаст таблицу в базе данных по текущему описанию модели
Для удаления таблицы:
`
from application.module_name.models import ModelName
from application.base.models import db
with db.allow_sync():
    ModelName.drop_table()
`
# CRUDL
Для реализации CRUDL следует использовать фреймворк Python-Rico
# Tests
Тестирование проводится с помощью фреймворка pytest (http://docs.pytest.org/en/latest/)
Все тесты связанные с тестированием обработчиков (handlers) проводятся в асинхронном режиме.
Для этого их необходимо обернуть декоратором @pytest.mark.gen_test
Дополнительные хелперы с описанием находтся в tests/conftest.py