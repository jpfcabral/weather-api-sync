FROM python:3.10

COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app

RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt


COPY ./app /app/app
EXPOSE 8000

CMD uvicorn app.main:app --host 0.0.0.0
