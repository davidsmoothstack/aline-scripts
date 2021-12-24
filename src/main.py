from requests.models import HTTPError
from bank import *
from helpers.util import get_env
from underwriter import *
from user import *


def authenticate(username, password):
    try:
        create_user(username, password)
    except HTTPError as e:
        if e.response.status_code == 409:
            print("User already exists")
            print("")
        else:
            raise e
    finally:
        login(username, password)


if __name__ == "__main__":
    try:
        username = get_env("ADMIN_USERNAME")
        password = get_env("ADMIN_PASSWORD")

        authenticate(username, password)

        bank = create_bank().json()
        create_branch(bank["id"])

        applicant = create_applicant()
        create_application()
    except Exception as e:
        print(f"{e}\n{e.response.text}")
