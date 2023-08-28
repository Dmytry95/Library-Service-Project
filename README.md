# Library-API-Service

Service for borrowing books with stripe payment system and notifications via telegram bot

## Installing process
Change mocks to your native data inside .env.sample. Do not forget to change file name to ".env".
#### Run with IDE
```
    git clone https://github.com/Dmytry95/Library-Service-Project.git
    cd LibraryService
    python -m venv venv
    sourse venv/bin/activate
    pip install -r requirements.txt
    set DJANGO_SECRET_KEY=your_django_secret_key
    set TELEGRAM_TOKEN=your_telegram_token
    set TELEGRAM_CHAT_ID=your_chat_id
    set STRIPE_SECRET_KEY=your_stripe_secret_key
    python manage.py migrate
    python manage.py runserver
```

## Run Redis/Celery/Celery-Beat
Docker should be installed locally to run Redis
#### Open terminal
```
    docker run -p 127.0.0.1:16379:6379 --name redis-celery -d redis
    celery -A library_service worker -l info --pool=solo -n worker@%h
    celery -A library_service beat -l INFO

```

## Getting access

* create user via /api/user/register
* get access token via api/user/login(do not forget to add "Bearer " before token)


## Features
* JWT authenticated
* Admin panel /admin/
* Managing borrowings depending on user stuff role
* Paying for borrowings with stripe
* Notifications via telegram bot
* Filtering borrowings by status and user
* Filtering books by author, title
