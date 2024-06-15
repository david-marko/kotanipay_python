import requests


class RequestsHandler:
    debug = None
    apiUrl = "https://api.kotanipay.io/api/v3"
    stagingUrl = "https://kpapistaging.api-service.live/api/v3"
    accessKey = None
    url = None
    headers = {"content-type": "application/json"}

    def __init__(self, accessToken=None, debug=True):
        self.accessKey = accessToken
        if accessToken:
            self.headers["Authorization"] = f"Bearer {accessToken}"
        self.debug = debug
        if debug:
            self.url = self.stagingUrl
        else:
            self.url = self.apiUrl

    def _make_request(self, method, endpoint, **kwargs):
        if self.accessKey is None:
            raise Exception("No access token provided")
        url = self.url + endpoint
        response = requests.request(method, url, headers=self.headers, **kwargs)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
