docker-up:
	docker compose up

docker-down:
	docker compose down

run:
	python manage.py runserver 0.0.0.0:8081

migrate:
	python manage.py makemigrations
	python manage.py migrate