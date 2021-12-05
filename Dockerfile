FROM python:3.8

WORKDIR usr/src/app

COPY . usr/src/app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "northbasketball.wsgi"]