from __future__ import absolute_import, unicode_literals
import time

from celery import shared_task
from celery_once import QueueOnce


@shared_task(base=QueueOnce)
def test_celery_beat():
    print('hello!')
    time.sleep(10)
