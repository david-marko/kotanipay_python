from pydantic import BaseModel, EmailStr
from typing import Optional


class WithdrawandDepositModel(BaseModel):
    customer_key: str
    amount: float
    walletId: str
    callbackUrl: Optional[str]
    referenceId: Optional[str]


class OffRampRequestModel(BaseModel):
    senders_address: str
    senders_amount: str
    chain: str
    tokens: str


class OffRampFiatRequestModel(BaseModel):
    transaction_hash: str
    chain: str
    token: str
    wallet_id: str
    preview: bool
    customer_key: str
    request_id: str
    callback_url: str
    referenceId: str


class OnRampFiatRequestModel(BaseModel):
    source_wallet: str
    recievers_address: str
    amount: str
    chain: str
    token: str
    preview: bool
    callback_url: str
