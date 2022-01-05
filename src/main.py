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


if __name__ == "__main__":
    try:
        username = get_env("ADMIN_USERNAME")
        password = get_env("ADMIN_PASSWORD")
        authenticate(username, password)

        bank = create_bank().json()
        create_branch(bank["id"])

        fake_app = fake_applicant()
        applicant = create_applicant(fake_app).json()
        application_result = create_application(applicant["id"]).json()

        (user, _) = random_userpass()
        membership_id = application_result["createdMembers"][0]["membershipId"]
        last_ssn = fake_app["socialSecurity"].rsplit("-")[2]
        account = create_user(
            user, password, isAdmin=False, membershipId=membership_id, lastFourSSN=last_ssn)

        for _ in range(100):
            try:
                # prompt user for account id
                create_transaction("0011015103")
            except Exception as e:
                print(e)

                if e.response.status_code == 404:
                    break

                continue

    except HTTPError as e:
        print(f"{e}\n{e.response.text}")
    except Exception as e:
        print(e)
