FROM python:3.10.2-slim

RUN apt-get update && apt install make

RUN pip install pipenv

WORKDIR /home/python/app

ENV PIPENV_VENV_IN_PROJECT=True

CMD [ "tail", "-f", "/dev/null" ]