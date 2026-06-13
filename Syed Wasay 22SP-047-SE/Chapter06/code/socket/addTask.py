import os
from celery import Celery

broker_url = os.environ.get('CELERY_BROKER_URL', 'sqla+sqlite:///celerydb.sqlite')
backend_url = os.environ.get('CELERY_RESULT_BACKEND', 'db+sqlite:///celerydb.sqlite')

app = Celery('tasks', broker=broker_url, backend=backend_url)

@app.task
def add(x, y):
    return x + y

