from __future__ import absolute_import, unicode_literals
import sys

from kombu import Connection, Producer, Exchange

def main(arguments):
    exchange = Exchange('celery', type='direct')
    with Connection('redis://localhost:6379/1') as conn:
        producer = Producer(conn)
        producer.publish([{'hello': 'world'}], exchange=exchange,
                         routing_key='celery', compression='zlib', serializer='json')

def run():
    sys.exit(main(sys.argv[1:]))
