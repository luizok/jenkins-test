from flask import Flask
import time
import requests
import threading
import logging


app = Flask(__name__)
fib_number = 0

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/<int:n>', methods=['GET'])
def main_route(n):

    global fib_number

    time.sleep(.5)
    fib_number += n
    print(f'New fibonacci number -> {fib_number}', flush=True)

    requests.get(f'http://nodejs_server/{fib_number}')

    return {'status': 200}


def main():

    print('Waiting...', flush=True)
    time.sleep(5)
    requests.get('http://nodejs_server/1')


if __name__ == '__main__':

    server = threading.Thread(target=app.run, kwargs={
        'host': '0.0.0.0',
        'port': 80,
        'debug': False
    })
    main = threading.Thread(target=main)

    main.run()
    server.run()
