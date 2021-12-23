from dataclasses import dataclass

from requests.api import request
from returns.io import impure_safe


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
        result = request(self.method, headers=self.headers, url=self.url, data=self.data)
        result.raise_for_status()
        return result
