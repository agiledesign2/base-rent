release: python manage.py migrate
#{% if cookiecutter.use_async == "y" -%}
#web: gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
#{%- else  %}
web: gunicorn config.wsgi:application --log-file -
#{%- endif %}
#{% if cookiecutter.use_celery == "y" -%}
#worker: celery worker --app=config.celery_app --loglevel=info
#beat: celery beat --app=config.celery_app --loglevel=info
#{%- endif %}