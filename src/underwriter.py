import random
from random import random

from faker import Faker

import helpers.store as store
import helpers.util as util
from helpers.RequestBuilder import RequestBuilder
from user import is_logged_in

fake = Faker()
base_url = util.base_from_env("DOMAIN", "UNDERWRITER_SERVICE_PORT")


def _fake_applicant():
    return {
        "address": fake.street_address(),
        "city": fake.city(),
        "dateOfBirth": fake.numerify("19##-0%-1#"),
        "driversLicense": fake.numerify("#########"),
        "email": fake.email(),
        "firstName": fake.first_name(),
        "gender": fake.random_element(elements=("MALE", "FEMALE", "OTHER", "UNSPECIFIED")),
        "income": fake.numerify("#%#######"),
        "lastName": fake.last_name(),
        "mailingAddress": fake.street_address(),
        "mailingCity": fake.city(),
        "mailingState": fake.state(),
        "mailingZipcode": fake.zipcode(),
        "middleName": fake.first_name(),
        "phone": fake.numerify("(###)-###-####"),
        "socialSecurity": fake.numerify("###-##-####"),
        "state": fake.state(),
        "zipcode": fake.zipcode()
    }


def _fake_application():
    return {
        "applicationType": fake.random_element(elements=("CHECKING", "SAVINGS", "CREDIT_CARD")),
        "noApplicants": False,
        "applicants": [_fake_applicant()]
    }


def create_applicant():
    if not is_logged_in():
        print("You need to be logged in before you can create an applicant")
        return

    json_applicant = util.to_json(_fake_applicant())

    return (RequestBuilder()
            .with_bearer_token(store.get_token())
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/applicants")
            .with_data(json_applicant)
            .execute_request())


def create_application():
    # TODO: Check if logged in
    json_application = util.to_json(_fake_application())

    return (RequestBuilder()
            .with_bearer_token(store.get_token())
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/applications")
            .with_data(json_application)
            .execute_request())
