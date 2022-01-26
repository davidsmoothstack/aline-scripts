from requests.models import HTTPError

from bank import create_bank, create_branch
from helpers.util import get_env
from transaction import create_transaction
from underwriter import create_applicant, create_application, fake_applicant
from user import create_user, login
from faker import Faker

fake = Faker()


def authenticate(username, password):
    try:
        create_user(username, password, isAdmin=True)
    except HTTPError as e:
        if e.response.status_code == 409:
            print("User already exists")
            print("")
        else:
            raise e
    finally:
        login(username, password)


def random_userpass():
    username = fake.user_name() + str(fake.random_digit())
    return (username, "P@ssword1")


def last_digits(ssn):
    """Gets the last four digits of a SSN"""
    return ssn.rsplit("-")[2]


def get_membership_id(application_result):
    return application_result["createdMembers"][0]["membershipId"]


if __name__ == "__main__":
    try:
        admin_username = get_env("ADMIN_USERNAME")
        admin_password = get_env("ADMIN_PASSWORD")
        authenticate(admin_username, admin_password)

        bank = create_bank().json()
        create_branch(bank["id"])

        fake_app = fake_applicant()
        applicant = create_applicant(fake_app).json()
        application_result = create_application(applicant["id"]).json()

        (random_username, random_password) = random_userpass()
        membership_id = get_membership_id(application_result)
        ssn_last = last_digits(fake_app["socialSecurity"])
        account = create_user(
            random_username,
            random_password,
            isAdmin=False,
            membershipId=membership_id,
            lastFourSSN=ssn_last)

        account_number = input("Account number to create a transaction with: ")
        create_transaction(account_number)
    except HTTPError as e:
        print(f"{e}\n{e.response.text}")
    except Exception as e:
        print(e)
