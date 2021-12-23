from dataclasses import dataclass
from requests.api import request

@dataclass(init=False)
class RequestBuilder():
    method: str
    url: str
    headers: dict[str]
    data: dict[str]

    def with_method(self, method):
        self.method = method
        return self

    def with_url(self, url):
        self.url = url
        return self

    def with_headers(self, headers):
        self.headers = headers
        return self

    def with_data(self, data):
        self.data = data
        return self

    def with_default_headers(self):
        self.headers = { "Content-Type": "application/json"}
        return self

    def execute_request(self):
        response = request(self.method, self.url, headers=self.headers, data=self.data)

        if not response.ok:
            raise Exception(f"{response.url} failed: {response.text}")

        print(f"{response.url} successful")

        if response.status_code == 201:
            print(response.json())
            print("")

        return response

# TODO: Remove
    # def print_response(response):
    #     if not response.ok:
    #         raise Exception(f"{response.url} failed: {response.text}")

    #     print(f"{response.url} successful")
    #     print("")

    #     if response.status_code == 201:
    #         print(response.json())
    #         print("")
    #         return response.json()

    #     return None
