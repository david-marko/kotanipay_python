from pydantic import BaseModel, EmailStr
from typing import Optional

class BioModel(BaseModel):
    first_name: str
    surname: str
    gender: str
    date_of_birth: str
    occupation: str
    country_code: str


class KYCModel(BaseModel):
    _type: str
    number: str


class AddressModel(BaseModel):
    line: str
    province: str
    municipality: str
    city: str


class ContactModel(BaseModel):
    phone_number: str
    email: EmailStr
    address: AddressModel


class BankCustomerModel(BaseModel):
    bio: BioModel
    kyc: KYCModel
    contact: ContactModel
    reference: str

class MobileCustomerModel(BaseModel):
    phone_number: str
    country_code: str
    network: Optional[str]
    account_name: Optional[str]


class MobileCustomerContactModel(BaseModel):
    phone_number: str
    network: Optional[str]
    account_name: Optional[str]
    country_code: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[str]
    id_number: Optional[str]
    image: Optional[str]
    id_type: Optional[str]

class KycDetailsModel(BaseModel):
    userEmail: EmailStr
    customerKey: str
    firstName: str
    lastName: str
    dob: str
    gender: str
    phone: str


class KycAddressModel(BaseModel):
    kycId: str
    street: str
    town: str
    country: str


class KycDocumentModel(BaseModel):
    kycId: str
    nationality: str
    documentNo: str
    documentExpiryDate: str
    country: str
    documentName: str