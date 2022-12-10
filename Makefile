docker-up:
	docker compose up -d

docker-down:
	docker compose down

install:
	pipenv install
	pipenv run python manage.py migrate
	pipenv run python manage.py loaddata initial_data

run:
	pipenv run python manage.py runserver 0.0.0.0:8081

migrate:
	python manage.py makemigrations
	python manage.py migrate