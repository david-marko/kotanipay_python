from pydantic import BaseModel


class FiatWalletModel(BaseModel):
    name: str
    currency: str  # Strict options


class CryptoWalletModel(BaseModel):
    name: str
    coin: str
    chain: str
