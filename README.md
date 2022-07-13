#### Stack:
- Django
- Docker

##### Инструкция для запуска бэкэнда:

==Важно!==

  - Устанавливаем докер eсли нету. 
    - (Если винда, то земля металлом, придется ставить wsl2)
    - (Если линукс, то надо ставить docker compose, в desktop версии он идет вкупе)
  - Возможно надо будет дать права, смотрим по ситуации, гуглим.


1) Копируем репу https://github.com/kisaragi99/yoko
2) Заходим в папку yoko
4) Пишем docker-compose up
5) В браузере заходим на http://localhost:8000/
6) Проверяем есть ли посередине надпись "The install worked successfully! Congratulations!"
7) Положить контейнеры - docker-compose stop


## What have been done:

1) Wrapped django app in docker container
2) Used dotenv for dynamic credentials (need to create .env file manually)


instruction for django and docker
==https://docs.docker.com/samples/django/==