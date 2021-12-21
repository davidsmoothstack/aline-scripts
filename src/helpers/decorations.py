
def print_response(func):
    def inner(*args):
        response = func(*args)

        if response.ok:
            print(f"{func.__name__} successful")

            if response.status_code == 201:
                print(response.json())
                print("")
                return response.json()

            print("")
        else:
            raise Exception(f"{func.__name__} failed: " + response.text)

    return inner
