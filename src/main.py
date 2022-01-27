import random
from faker import Faker
from requests.models import HTTPError

import bank
import transaction
import underwriter
import user
from helpers.util import get_env, repeat

fake = Faker()


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


def random_userpass():
    username = fake.user_name() + str(fake.random_digit())
    return (username, "P@ssword1")


def user_generator():
    fake_app = underwriter.create_applicant(
        underwriter.fake_applicant()).json()

    application_result = underwriter.create_application(fake_app["id"]).json()

    (random_username, random_password) = random_userpass()
    membership_id = application_result["createdMembers"][0]["membershipId"]
    ssn_last = fake_app["socialSecurity"].rsplit("-")[2]

    account = user.create_user(
        random_username,
        random_password,
        isAdmin=False,
        membershipId=membership_id,
        lastFourSSN=ssn_last).json()

    return (account, application_result)


def branch_generator(banks):
    random_bank = random.choice(banks)
    return bank.create_branch(random_bank["id"]).json()


def transaction_generator(application_results):
    random_application = random.choice(application_results)
    random_account_number = random.choice(
        random_application["createdAccounts"])["accountNumber"]

    return transaction.create_transaction(random_account_number).json()


if __name__ == "__main__":
    try:
        admin_username = get_env("ADMIN_USERNAME")
        admin_password = get_env("ADMIN_PASSWORD")
        authenticate(admin_username, admin_password)

        banks = repeat("How many banks should be created?",
                       lambda: bank.create_bank().json())

        branches = repeat("How many branches should be created?",
                          lambda: branch_generator(banks))

        user_application_result_pairs = repeat("How many users should be created?",
                                               lambda: user_generator())

        application_results = list(
            map(lambda pair: pair[1],
                user_application_result_pairs))

        account_number = repeat("How many transactions should be created?",
                                lambda: transaction_generator(application_results))
    except HTTPError as e:
        print(f"{e}\n{e.response.text}")
    except Exception as e:
        print(e)
