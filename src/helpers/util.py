import json
import os
import random

from functional import seq


def _get_env(env):
    result = os.getenv(env)

    if result is None:
        raise Exception(f"Environment variable '{env}' has no value")

    return result


def to_json(input):
    return json.dumps(input)


def full_url(base_url, endpoint):
    f"{base_url}/{endpoint}"


def base_from_env(domain_env, port_env):
    domain = _get_env(domain_env)
    port = _get_env(port_env)
    return f"{domain}:{port}"
