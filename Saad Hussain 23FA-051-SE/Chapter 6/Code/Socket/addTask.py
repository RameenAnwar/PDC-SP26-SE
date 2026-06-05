from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.conf.worker_enable_remote_control = False

@app.task
def add(x, y):
    return x + y
