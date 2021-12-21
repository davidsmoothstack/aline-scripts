import json

import requests
from faker import Faker
from functional import util

import helpers.data as data
import helpers.util as util
from helpers.decorations import print_response

fake = Faker()

url = "http://localhost:8070"


@print_response
def create_user(username, password, isAdmin):
    path = "/users/registration"

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}.{last_name}@example.com"

    return requests.request("POST",
                            url + path,
                            headers={
                                'Content-Type': 'application/json'
                            },
                            data=json.dumps({
                                "role": "admin" if isAdmin else "member",
                                "username": username,
                                "password": password,
                                "firstName": fake.first_name(),
                                "lastName": fake.last_name(),
                                "email": email,
                                "phone": util.phone_number(),
                                "membershipId": 1,
                                "lastFourOfSSN": 1111
                            }))


@print_response
def login(username, password):
    path = "/login"

    response = requests.request(
        "POST",
        url + path,
        headers={
            'Content-Type': 'application/json'
        }, data=json.dumps({
            "username": username,
            "password": password
        })
    )

    if response.ok:
        data.set_value("token", response.headers["Authorization"])

    return response


def isLoggedIn():
    if data.get_value("token") is None:
        return False
    else:
        return True
