from __future__ import absolute_import, unicode_literals
import time

from celery import shared_task


@shared_task
def test_celery_beat():
    print('hello!')
    time.sleep(10)
