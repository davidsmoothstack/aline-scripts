import json
from random import random

import requests
from faker import Faker

import helpers.data as data
from helpers.decorations import *
from user import isLoggedIn
import helpers.util as util

import random

url = "http://localhost:8071"
fake = Faker()


@print_response
def create_applicant():
    if not isLoggedIn():
        print("You need to be logged in before you can create an applicant")
        return

    path = "/applicants"

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}.{last_name}@example.com"

    response = requests.request(
        "POST", 
        url + path,
        headers={
            'Authorization': data.get_value("token"),
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            "firstName": first_name,
            "middleName": None,
            "lastName": last_name,
            "dateOfBirth": "1990-01-01",
            "gender": "UNSPECIFIED",
            "email": email,
            "phone": util.phone_number(),
            "socialSecurity": fake.ssn(),
            "driversLicense": util.drivers_liscense(),
            "income": random.randrange(5_000, 500_000),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": "TX",
            "zipcode": 11111,
            "mailingAddress": fake.street_address(),
            "mailingCity": fake.city(),
            "mailingState": "TX",
            "mailingZipcode": 11111
        }))

    return response


@print_response
def create_application(applicatonType, applicants):
    path = "/applications"

    response = requests.request(
        "POST",
        url + path,
        headers={
            'Authorization': data.get_value("token"),
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            "applicationType": applicatonType,
            "noApplicants": True,
            "applicantIds": [3],
            "applicants": None
        }))

    return response
