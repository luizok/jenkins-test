from flask import Flask
import time
import requests
from multiprocessing import Process
import logging


app = Flask(__name__)
fib_number = 0

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def increment_fib(n):

    global fib_number

    fib_number += n

    return fib_number


@app.route('/<int:n>', methods=['GET'])
def main_route(n):

    time.sleep(.5)
    increment_fib(n)
    print(f'New fibonacci number -> {fib_number}', flush=True)

    requests.get(f'http://nodejs_server/{fib_number}')

    return {'status': 200}


def main():

    print('Waiting...', flush=True)
    time.sleep(5)
    requests.get('http://nodejs_server/1')


if __name__ == '__main__':

    server = Process(target=app.run, kwargs={
        'host': '0.0.0.0',
        'port': 80,
        'debug': False
    })
    main = Process(target=main)

    main.start()
    server.start()
