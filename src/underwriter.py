from faker import Faker

import helpers.store as store
import helpers.util as util
from helpers.RequestBuilder import RequestBuilder

__fake = Faker()
base_url = util.base_from_env("DOMAIN", "UNDERWRITER_SERVICE_PORT")


def __fake_applicant():
    return {
        "address": __fake.street_address(),
        "city": __fake.city(),
        "dateOfBirth": __fake.numerify("19##-0%-1#"),
        "driversLicense": __fake.numerify("#########"),
        "email": __fake.email(),
        "firstName": __fake.first_name(),
        "gender": __fake.random_element(elements=("MALE", "FEMALE", "OTHER", "UNSPECIFIED")),
        "income": __fake.numerify("#%#######"),
        "lastName": __fake.last_name(),
        "mailingAddress": __fake.street_address(),
        "mailingCity": __fake.city(),
        "mailingState": __fake.state(),
        "mailingZipcode": __fake.zipcode(),
        "middleName": __fake.first_name(),
        "phone": __fake.numerify("(###)-###-####"),
        "socialSecurity": __fake.numerify("###-##-####"),
        "state": __fake.state(),
        "zipcode": __fake.zipcode()
    }


def __fake_application_request():
    return {
        "applicationType": __fake.random_element(elements=("CHECKING", "SAVINGS", "CREDIT_CARD")),
        "noApplicants": False,
        "applicants": [__fake_applicant()]
    }


@util.auth_guard
def create_applicant():
    json_applicant = util.to_json(__fake_applicant())

    return (RequestBuilder()
            .with_bearer_token(store.get_token())
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/applicants")
            .with_data(json_applicant)
            .execute_request())


def create_application():
    # TODO: Check if logged in
    json_application = util.to_json(__fake_application_request())

    return (RequestBuilder()
            .with_bearer_token(store.get_token())
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/applications")
            .with_data(json_application)
            .execute_request())
