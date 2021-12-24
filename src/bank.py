from faker import Faker

import helpers.store as store
import helpers.util as util
from helpers.RequestBuilder import RequestBuilder
from user import is_logged_in

fake = Faker()
base_url = util.base_from_env("DOMAIN", "BANK_SERVICE_PORT")
token = store.get_value("token")


def _fake_bank():
    return {
        "routingNumber": fake.aba(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zipcode": fake.numerify("#####")
    }


def _fake_branch(bankId):
    return {
        "name": fake.name(),
        "phone": fake.numerify("(###)-###-####"),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zipcode": fake.numerify("#####"),
        "bankID": bankId
    }


def create_bank():
    if not is_logged_in():
        print("You need to be logged in before you can create a bank")
        return

    bank_json = util.to_json(_fake_bank())

    return (RequestBuilder()
            .with_bearer_token(token)
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/banks")
            .with_data(bank_json)
            .execute_request())


def create_branch(bankId):
    if not is_logged_in():
        print("You need to be logged in before you can create a branch")
        return

    branch_json = util.to_json(_fake_branch(bankId))

    return (RequestBuilder()
            .with_bearer_token(token)
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/branches")
            .with_data(branch_json)
            .execute_request())
