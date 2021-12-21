import json

import requests
from faker import Faker

import helpers.data as data
from helpers.decorations import *
from user import isLoggedIn

fake = Faker()
url = "http://localhost:8083"


@print_response
def create_bank():
    if not isLoggedIn():
        print("You need to be logged in before you can create a bank")
        return

    path = "/banks"

    response = requests.request("POST",
                                url + path,
                                headers={
                                    'Authorization': data.get_value("token"),
                                    'Content-Type': 'application/json'
                                },
                                data=json.dumps({
                                    "routingNumber": fake.aba(),
                                    "address": fake.street_address(),
                                    "city": fake.city(),
                                    "state": "TX",
                                    "zipcode": "11111"
                                }))

    return response


@print_response
def create_branch(bankId):
    if not isLoggedIn():
        print("You need to be logged in before you can create a branch")
        return

    path = "/branches"

    response = requests.request(
        "POST",
        url + path,
        headers={
            'Authorization': data.get_value("token"),
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            "name": "branch",
            "phone": fake.phone_number(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": "TX",
            "zipcode": "11111",
            "bankID": bankId
        }))

    return response
