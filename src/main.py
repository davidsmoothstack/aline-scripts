from faker import Faker
from requests.models import HTTPError

import bank
import transaction
import underwriter
import user
from helpers.util import get_env, repeat

fake = Faker()


def random_userpass():
    username = fake.user_name() + str(fake.random_digit())
    return (username, "P@ssword1")


def last_digits(ssn):
    """Gets the last four digits of a SSN"""
    return ssn.rsplit("-")[2]


def get_membership_id(application_result):
    return application_result["createdMembers"][0]["membershipId"]


def authenticate(username, password):
    """Creates admin account if if does not exist, then stores the credentials locally"""
    try:
        user.create_user(username, password, isAdmin=True)
    except HTTPError as e:
        if e.response.status_code == 409:
            print("User already exists")
            print("")
        else:
            raise e
    finally:
        user.login(username, password)


def user_generator():
    fake_app = underwriter.create_applicant(
        underwriter.fake_applicant()).json()

    application_result = underwriter.create_application(fake_app["id"]).json()

    (random_username, random_password) = random_userpass()
    membership_id = get_membership_id(application_result)
    ssn_last = last_digits(fake_app["socialSecurity"])
    account = user.create_user(
        random_username,
        random_password,
        isAdmin=False,
        membershipId=membership_id,
        lastFourSSN=ssn_last)

    return account


def bank_generator():
    pass


def branch_generator(banks):
    pass


if __name__ == "__main__":
    try:
        admin_username = get_env("ADMIN_USERNAME")
        admin_password = get_env("ADMIN_PASSWORD")
        authenticate(admin_username, admin_password)

        banks = repeat("How many banks should be created?",
                       lambda: bank.create_bank().json())

        branches = repeat("How many branches should be created?",
                          lambda: bank.create_branch(banks[0]["id"]).json())

        users = repeat("How many users should be created?",
                       lambda: user_generator())

        account_number = input("Account number to create a transaction with: ")

        transaction.create_transaction(account_number)
    except HTTPError as e:
        print(f"{e}\n{e.response.text}")
    except Exception as e:
        print(e)
