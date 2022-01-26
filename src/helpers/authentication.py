import helpers.store as store

token_key = "token"


def get_token():
    return store.get_value(token_key)


def set_token(val):
    store.set_value(token_key, val)


def is_logged_in():
    return store.get_token() is not None


def auth_guard(func):
    def decorator(*args):
        if is_logged_in() == False:
            raise Exception(
                f"You need to be authenticated before you can call '{func.__name__}'")

        return func(*args)

    return decorator
