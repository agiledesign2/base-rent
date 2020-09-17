FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements/base.txt base.txt ./
COPY ./requirements/local.txt ./
RUN pip install -r production.txt

# Adds our application code to the image
#RUN mkdir ./code
COPY . ./code
WORKDIR ./code

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - piedpiper.wsgi:application
#CMD python manage.py runserver 0.0.0.0:$PORT 		#take port from Heroku
