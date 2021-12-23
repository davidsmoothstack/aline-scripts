import random
from random import random

from faker import Faker

import helpers.data as data
import helpers.util as util
from helpers.RequestBuilder import RequestBuilder
from user import isLoggedIn

fake = Faker()
base_url = util.base_from_env("DOMAIN", "UNDERWRITER_SERVICE_PORT")
token = data.get_value("token")


def _fake_applicant():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}.{last_name}@example.com"

    return {
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
    }


def _fake_application(applicatonType):
    return {
        "applicationType": applicatonType,
        "noApplicants": True,
        "applicantIds": [3],
        "applicants": None
    }


def create_applicant():
    if not isLoggedIn():
        print("You need to be logged in before you can create an applicant")
        return

    return (RequestBuilder()
            .with_bearer_token(token)
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/applicants")
            .with_data(_fake_applicant())
            .execute_request())


def create_application(applicatonType="CHECKING"):
    return (RequestBuilder()
            .with_bearer_token(token)
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/applications")
            .with_data(_fake_application(applicatonType))
            .execute_request())
