from kotanipay_sdk.config import RequestsHandler
from .walletModels import FiatWalletModel, CryptoWalletModel


class Wallet(RequestsHandler):
    wallet_type = "crypto"  # | Fiat
    walletId = None

    def __init__(self, accessToken=None, debug=True, wallet_type="crypto"):
        self.wallet_type = wallet_type
        RequestsHandler.__init__(self, accessToken, debug)

    def createWallet(self, data: FiatWalletModel | CryptoWalletModel):
        endpoint = f"/wallet/{self.wallet_type}"
        return self._make_request("POST", endpoint, json=data)

    def getWallets(self):
        endpoint = f"/wallet/{self.wallet_type}"
        return self._make_request("GET", endpoint)

    def getWallet(self):
        endpoint = f"/wallet/{self.wallet_type}/{self.walletId}"
        return self._make_request("GET", endpoint)

    def getAddressDetails(self):
        # Only for crypto wallets
        endpoint = f"/wallet/crypto/request-details/{self.walletId}"
        return self._make_request("GET", endpoint)

    def updateWallet(self, name: str):
        endpoint = f"/wallet/{self.wallet_type}/{self.walletId}"
        payload = {"name": name}
        return self._make_request("PATCH", endpoint, json=payload)
