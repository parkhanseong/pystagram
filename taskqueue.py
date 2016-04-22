import time
import os

from PIL import Image
from celery import Celery

app = Celery(
    'taskqueue',
    broker='redis://localhost:6379/0',
    brackend='redis://localhost:6379/0',
)

def make_thumbnail(path, width, height):
    filepath, ext = os.path.splitext(path)
    output_path = '{}_thumb{}'.format(filepth, ext)

    if os.path.exitsts(output_path):
        return output_path

    im = Image.open(path)
    im.thumbnail((width, height,), Image.ANTIALIAS)
    im.save(output_path)
    im.close()

    return output_path


@app.task
def add(a,b):
    time.sleep(5)
    return a+b

@app.task
def sum2(values):
    time.sleep(5)
    return sum(value)
