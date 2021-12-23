from bank import *
from underwriter import *
from user import *

if __name__ == "__main__":
    username = "TheAdmin"
    password = "P@$$word1"

    try:
        create_user(username, password)
    except Exception as e:
        print(e)
        print("")

    try:
        login(username, password)

        bank = create_bank().json()
        create_branch(bank["id"])

        applicant = create_applicant()
        create_application("CHECKING", [applicant])
    except Exception as e:
        print(e)
