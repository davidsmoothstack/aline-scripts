from faker import Faker

import helpers.store as store
import helpers.util as util
from helpers.authentication import auth_guard
from helpers.RequestBuilder import RequestBuilder

__fake = Faker()
base_url = util.base_from_env("DOMAIN", "BANK_SERVICE_PORT")


def __fake_bank():
    return {
        "routingNumber": __fake.aba(),
        "address": __fake.street_address(),
        "city": __fake.city(),
        "state": __fake.state(),
        "zipcode": __fake.numerify("#####")
    }


def __fake_branch(bankId):
    return {
        "name": __fake.name(),
        "phone": __fake.numerify("(###)-###-####"),
        "address": __fake.street_address(),
        "city": __fake.city(),
        "state": __fake.state(),
        "zipcode": __fake.numerify("#####"),
        "bankID": bankId
    }


@auth_guard
def create_bank():
    bank_json = util.to_json(__fake_bank())

    return (RequestBuilder()
            .with_bearer_token(store.get_token())
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/banks")
            .with_data(bank_json)
            .execute_request())


@auth_guard
def create_branch(bankId):
    branch_json = util.to_json(__fake_branch(bankId))

    return (RequestBuilder()
            .with_bearer_token(store.get_token())
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/branches")
            .with_data(branch_json)
            .execute_request())
