from faker import Faker
from functional import util
from requests.models import Response

import helpers.store as store
import helpers.util as util
from helpers.RequestBuilder import RequestBuilder

__fake = Faker()
base_url = util.base_from_env("DOMAIN", "USER_SERVICE_PORT")


def __fake_user(username, password, isAdmin):
    return {
        "role": "admin" if isAdmin else "member",
        "username": username,
        "password": password,
        "firstName": __fake.first_name(),
        "lastName": __fake.last_name(),
        "email": __fake.email(),
        "phone": __fake.numerify('(###)-###-####'),
        "membershipId": 0,  # TODO: Look into
        "lastFourOfSSN": 1111
    }


def create_user(username, password, isAdmin=True) -> Response:
    json_user = util.to_json(__fake_user(username, password, isAdmin))

    return (RequestBuilder()
            .with_default_headers()
            .with_method("POST")
            .with_url(base_url + "/users/registration")
            .with_data(json_user)
            .execute_request())


def login(username, password) -> Response:
    json_credentials = util.to_json(
        {"username": username, "password": password})

    response = (RequestBuilder()
                .with_default_headers()
                .with_method("POST")
                .with_url(base_url + "/login")
                .with_data(json_credentials)
                .execute_request())

    store.set_token(response.headers.get("Authorization"))

    return response


def is_logged_in():
    return store.get_token() is not None
