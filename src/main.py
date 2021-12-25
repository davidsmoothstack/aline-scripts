from requests.models import HTTPError
from bank import create_bank, create_branch
from helpers.util import get_env
from underwriter import create_applicant, create_application
from user import create_user, login


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

        create_applicant()
        create_application()
    except HTTPError as e:
        print(f"{e}\n{e.response.text}")
    except Exception as e:
        print(e)
