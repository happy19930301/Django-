from __future__ import absolute_import, unicode_literals
import sys

from kombu import Connection

def main(arguments):
    with Connection('redis://localhost:6379/1') as conn:
        with conn.SimpleQueue('celery') as queue:
            message = queue.get(block=True, timeout=10)
            message.ack()
            print(message.payload)

def run():
    sys.exit(main(sys.argv[1:]))
