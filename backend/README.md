insurance_calculator/
│── alembic/                  # миграции БД
│── app/
│   │── __init__.py
│   │── main.py                # точка входа в приложение FastAPI
│   │── config.py              # конфигурация (БД, JWT, CORS и пр.)
│   │
│   ├── core/                  # ядро приложения (базовые штуки)
│   │   │── __init__.py
│   │   │── security.py        # JWT, хеширование паролей
│   │   │── database.py        # подключение к БД, сессии
│   │   │── logging.py         # логирование, middleware для ошибок
│   │
│   ├── models/                # модели ORM (SQLAlchemy)
│   │   │── __init__.py
│   │   │── user.py
│   │   │── quote.py
│   │   │── application.py
│   │
│   ├── schemas/               # Pydantic-схемы (валидация/сериализация)
│   │   │── __init__.py
│   │   │── auth.py
│   │   │── user.py
│   │   │── quote.py
│   │   │── application.py
│   │
│   ├── crud/                  # работа с БД (CRUD-логика)
│   │   │── __init__.py
│   │   │── user.py
│   │   │── quote.py
│   │   │── application.py
│   │
│   ├── routers/               # маршруты API (эндпоинты)
│   │   │── __init__.py
│   │   │── auth.py
│   │   │── user.py
│   │   │── quote.py
│   │   │── application.py
│   │
│   ├── services/              # бизнес-логика (например, калькуляция)
│   │   │── __init__.py
│   │   │── calculator.py
│   │
│   └── utils/                 # вспомогательные функции
│       │── __init__.py
│       │── validators.py      # кастомная валидация
│       │── responses.py       # единый формат ошибок/ответов
│
│── docker-compose.yml         # docker: postgres + api
│── Dockerfile                 # сборка приложения
│── pyproject.toml / requirements.txt
│── README.md                  # документация
