import os
import requests
import json
from flask import Flask, request, Response
import time
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')

registered_service = {}


def generate_random_string(service_name: str):
    size = 10
    chars = "abcdefghijklmn12345678" + str(int(time.time()))
    generated = ''.join(random.choice(chars) for _ in range(size))
    return generated + "_" + service_name


@app.route('/service/<name>', methods=["PUT"])
def register_service(name: str):

    client_id = generate_random_string("client_id_" + name)
    client_secret = generate_random_string("client_secret_" + name)

    registered_service[name] = {"client_id": client_id, "client_secret": client_secret}

    return registered_service


def generate_authorization_code(service_name: str):
    size = 10
    chars = "abcdefghijklmn12345678" + str(int(time.time()))
    generated = ''.join(random.choice(chars) for _ in range(size))
    return generated + "_" + service_name


@app.route('/login/', methods=["POST"])
def login():
    request_data = request.get_json()
    id = request_data['id']
    password = request_data['password']
    service_name = request_data['service_name']

    token = generate_authorization_code(service_name)
    res = {'token': token}
    return Response(
        json.dumps(res),
        mimetype="application/json",
        status=200,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config["PORT"])
