from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
# from celery_once import QueueOnce

from utils.web_setting import own_setting

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CODE.settings')

app = Celery('CODE')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'beatTest': {
        'task': 'netdisc.tasks.test_celery_beat',
        'schedule': timedelta(seconds=1),
        'args': ()
    },
}

app.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': 'redis://{}:{}/1'.format(own_setting.REDIS_HOST,
                                        own_setting.REDIS_PORT),
        'default_timeout': 5 * 60
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
