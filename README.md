Django app using PostgresSQL as DB, deployed using Docker.

Need to set up .env

 - DJANGO_SECRET_KEY = 
 - postgres_password = 
 - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
 - DEBUG=1
 - SQL_ENGINE=django.db.backends.postgresql
 - SQL_DATABASE=hello_django_dev
 - SQL_USER=
 - SQL_PASSWORD=
 - SQL_HOST=db
 - SQL_PORT=5432
 - DATABASE=postgres

The app will be up and available on localhost:

Can be run with:

docker-compose up -d --build