from faker import Faker

import helpers.util as util
from helpers.RequestBuilder import RequestBuilder

__fake = Faker()
base_url = util.base_from_env("DOMAIN", "TRANSACTION_SERVICE_PORT")


def __fake_transaction(accountNumber):
    return {
        "amount": __fake.numerify("#####"),
        "date": __fake.numerify("201#-0%-1#"),
        "initialBalance": __fake.numerify("####"),
        "method": __fake.random_element(elements=("ACH", "ATM", "CREDIT_CARD", "DEBIT_CARD", "APP")),
        "merchantCode": "1111",
        "type": __fake.random_element(elements=("WITHDRAWAL", "TRANSFER_OUT", "TRANSFER_IN", "DEPOSIT")),
        "accountNumber": accountNumber
    }


def create_transaction():
    # TODO: Remove magic number
    transaction_json = util.to_json(__fake_transaction(35365102))

    return (RequestBuilder()
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/transactions")
            .with_data(transaction_json)
            .execute_request())
