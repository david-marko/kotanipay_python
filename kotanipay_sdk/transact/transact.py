from kotanipay_sdk.config import RequestsHandler
from .transactModels import (
    WithdrawandDepositModel,
    OnRampFiatRequestModel,
    OffRampFiatRequestModel,
    OffRampRequestModel,
)


class Transact(RequestsHandler):
    reference_id = None

    def __init__(self, accessToken=None, debug=True):
        RequestsHandler.__init__(self, accessToken, debug)

    def depositToMobileMoney(self, depositOptions: WithdrawandDepositModel):
        endpoint = f"/deposit/mobile-money"
        return self._make_request("POST", endpoint, json=depositOptions)

    def depostStatus(self):
        endpoint = f"/deposit/mobile-money/status/{self.reference_id}"
        return self._make_request("GET", endpoint)

    def getRate(self, _from: str, _to: str):
        endpoint = f"/rate/{_from}/{_to}"
        return self._make_request("GET", endpoint)

    def getAllRates(self):
        endpoint = f"/rate"
        return self._make_request("GET", endpoint)

    def withdrawToMobileMoney(self, withdrawOptions: WithdrawandDepositModel):
        endpoint = f"/withdraw/mobile-money"
        return self._make_request("POST", endpoint, json=withdrawOptions)

    def withdrawStatus(self):
        endpoint = f"/withdraw/mobile-money/status/{self.reference_id}"
        return self._make_request("GET", endpoint)

    def onrampSend(self, req: OnRampFiatRequestModel):
        endpoint = f"/onramp/fiat-to-crypto/wallet"
        return self._make_request("POST", endpoint, json=req)

    def onrampStatus(self):
        endpoint = f"/onramp/fiat-to-crypto/wallet/status/{self.reference_id}"
        return self._make_request("GET", endpoint)

    def offrampRequest(self, req: OffRampRequestModel):
        endpoint = f"/offramp/crypto-to-fiat/mobile-money/request"
        return self._make_request("POST", endpoint, json=req)

    def offrampSend(self, req: OffRampFiatRequestModel):
        endpoint = f"/offramp/crypto-to-fiat/mobile-money"
        return self._make_request("POST", endpoint, json=req)

    def offrampStatus(self):
        endpoint = f"/offramp/crypto-to-fiat/mobile-money/status/{self.reference_id}"
        return self._make_request("GET", endpoint)

    def supportedChains(self):
        endpoint = f"/offramp/crypto-to-fiat/supported-chains"
        return self._make_request("GET", endpoint)
