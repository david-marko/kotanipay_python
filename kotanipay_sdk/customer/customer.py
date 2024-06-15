from kotanipay_sdk.config import RequestsHandler
from .customerModels import (
    BankCustomerModel,
    MobileCustomerModel,
    BioModel,
    ContactModel,
    KYCModel,
    MobileCustomerContactModel,
    KycAddressModel,
    KycDetailsModel,
    KycDocumentModel,
)


class Customer(RequestsHandler):
    customer_type = "bank"  # | 'mobile-money'
    customerKey = None

    def __init__(self, accessToken=None, debug=True, customer_type="bank"):
        self.customer_type = customer_type
        RequestsHandler.__init__(self, accessToken, debug)

    def createCustomer(self, customer: BankCustomerModel | MobileCustomerModel):
        endpoint = f"/customer/{self.customer_type}"
        return self._make_request("POST", endpoint, json=customer)

    def getAll(self):
        endpoint = f"/customer/{self.customer_type}"
        return self._make_request("GET", endpoint)

    def getCustomer(self):
        endpoint = f"/customer/{self.customer_type}/{self.customerKey}"
        return self._make_request("GET", endpoint)

    def getCustomerByPhone(self, phone_number: str):
        endpoint = f"/customer/{self.customer_type}/{phone_number}"
        return self._make_request("GET", endpoint)

    def updateBioData(self, bio: BioModel):
        endpoint = f"/customer/bank/bio/{self.customerKey}"
        return self._make_request("PATCH", endpoint, json=bio)

    def updateContactData(self, contact: ContactModel):
        endpoint = f"/customer/bank/contact/{self.customerKey}"
        return self._make_request("PATCH", endpoint, json=contact)

    def updateKYCData(self, kyc: KYCModel):
        endpoint = f"/customer/bank/kyc/{self.customerKey}"
        return self._make_request("PATCH", endpoint, json=kyc)

    def updateCustomerData(self, bio: MobileCustomerContactModel):
        endpoint = f"/customer/mobile-money/bio/{self.customerKey}"
        return self._make_request("PATCH", endpoint, json=bio)

    def basicDetails(self, details: KycDetailsModel):
        endpoint = f"/kyc"
        return self._make_request("POST", endpoint, json=details)

    def addressDetails(self, address: KycAddressModel):
        endpoint = f"/kyc/address"
        return self._make_request("POST", endpoint, json=address)

    def documentDetails(self, docs: KycDocumentModel):
        endpoint = f"/kyc/document"
        return self._make_request("POST", endpoint, json=docs)

    def kycStatus(self, kycId: str):
        endpoint = f"/kyc/status/{kycId}"
        return self._make_request("GET", endpoint)

    def kycUsers(self):
        endpoint = f"/kyc/integrator/users"
        return self._make_request("GET", endpoint)
