from requests import Response, post, get, put, patch, delete


class Api:
    _URL: str

    def __init__(self, url: str):
        self._URL = url

    def get(self, path: str, params: dict = {}, headers: dict = {}) -> Response:
        return get(f"{self._URL}{path}", params=params, headers=headers)

    def post(
        self, path: str, params: dict = {}, payload: dict = {}, headers: dict = {}
    ) -> Response:
        return post(f"{self._URL}{path}", params=params, data=payload, headers=headers)

    def put(
        self, path: str, params: dict = {}, payload: dict = {}, headers: dict = {}
    ) -> Response:
        return put(f"{self._URL}{path}", params=params, data=payload, headers=headers)

    def patch(
        self, path: str, params: dict = {}, payload: dict = {}, headers: dict = {}
    ) -> Response:
        return patch(f"{self._URL}{path}", params=params, data=payload, headers=headers)

    def delete(
        self, path: str, params: dict = {}, payload: dict = {}, headers: dict = {}
    ) -> Response:
        return delete(
            f"{self._URL}{path}", params=params, data=payload, headers=headers
        )
