from bank import *
from user import *
from underwriter import *


if __name__ == "__main__":
    try:
        create_user()
    except Exception as e:
        print(e)
        print("")

    try:
        login(username, password)

        bank = create_bank()
        create_branch(bank["id"])

        applicant = create_applicant()
        create_application("CHECKING", [applicant])
    except Exception as e:
        print(e)
