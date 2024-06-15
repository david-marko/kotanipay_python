from kotanipay_sdk import KotaniPay

access_key = ""

k = KotaniPay(accessToken=access_key, debug=False)

print(k.healthCheck())
