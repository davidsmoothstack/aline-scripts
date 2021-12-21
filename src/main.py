from bank import *
from user import *
from underwriter import *


if __name__ == "__main__":
    username = "PeterParker"
    password = "P@$$word1"

    try:
        create_user(username, password, True)
    except Exception as e:
        print(e)
        print("")

    try:
        login(username, password)
        login(username, password)

        bank = create_bank()
        create_branch(bank["id"])

        applicant = create_applicant()
        create_application("CHECKING", [applicant])
    except Exception as e:
        print(e)
