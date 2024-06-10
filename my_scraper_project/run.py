#import os
from threading import Thread
import time
import requests
from app import create_app
import logging

logging.basicConfig(level=logging.INFO)

app = create_app()


def run_flask():
    app.run(host='0.0.0.0', port=5005)


if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.start()

    time.sleep(5)

    try:
        response = requests.get('http://127.0.0.1:5005/scrape')
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as e:
        logging.error("Erro ao fazer a requisição GET: %s", e)