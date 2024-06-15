import requests
from pydantic import BaseModel
from .models import Integrator
from kotanipay_sdk.customer.customer import Customer
from kotanipay_sdk.wallet.wallet import Wallet
from kotanipay_sdk.transact.transact import Transact
from kotanipay_sdk.config import RequestsHandler


class KotaniPay(RequestsHandler):

    def __init__(self, accessToken=None, debug=True):
        self.accessKey = accessToken
        self.debug = debug
        RequestsHandler.__init__(self, self.accessKey, self.debug)
        self.Customer: Customer = Customer(self.accessKey, self.debug)
        self.Wallet = Wallet(self.accessKey, self.debug)
        self.Transact = Transact(self.accessKey, self.debug)

    def healthCheck(self):
        url = self.url[:-7] + "/health"  # removing the /v3 postfix
        response = requests.request("GET", url)
        return self._handle_response(response)

    def createIntegrator(self, integrator: Integrator):
        endpoint = f"/integrator"
        return self._make_request("POST", endpoint, json=integrator)

    def getIntegrators(self):
        endpoint = f"/integrator"
        return self._make_request("GET", endpoint)

    def login(self, email):
        url = self.url + "/auth/login"
        response = requests.request("POST", url, json={"email": email})
        return self._handle_response(response)

    def verifyAccount(self, hash):
        url = self.url + "/auth/verify?hash=" + hash
        response = requests.request("GET", url)
        return self._handle_response(response)
