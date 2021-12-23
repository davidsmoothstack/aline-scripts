from dataclasses import dataclass

from requests.api import request

import helpers.data as data


@dataclass()
class RequestBuilder():
    method: str
    url: str
    headers: dict[str]
    data: dict[str]

    def __init__(self) -> None:
        self.headers = {}

    def with_method(self, method):
        self.method = method
        return self

    def with_url(self, url):
        self.url = url
        return self

    def with_header(self, header):
        self.headers.update(header)
        return self

    def with_data(self, data):
        self.data = data
        return self

    def with_default_headers(self):
        self.headers.update({"Content-Type": "application/json"})
        return self

    def with_bearer_token(self, token):
        self.headers.update({"Authorization": token})
        return self

    def execute_request(self):
        response = request(self.method, self.url,
                           headers=self.headers, data=self.data)

        if not response.ok:
            raise Exception(f"{response.url} failed: {response.text}")

        print(f"{response.url} successful")

        if response.status_code == 201:
            print(response.json())
            print("")

        return response
