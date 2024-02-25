import hashlib
from hashlib import pbkdf2_hmac
import hmac
import json
def computeSha512(txtohas1,txtToHash):
  m = hmac.HMAC(txtohas1,txtToHash,digestmod=hashlib.sha512)
  return m.hexdigest()

clientSecret = '91MUDL9N6U3BQRXBQ2PJ9M0PW4J22M1Y'
requestBody ='{"eventData":{"product":{"reference":"111222333","type":"OFFLINE_PAYMENT_AGENT"},"transactionReference":"MNFY|76|20211117154810|000001","paymentReference":"0.01462001097368737","paidOn":"17/11/2021 3:48:10 PM","paymentDescription":"Mockaroo Jesse","metaData":{},"destinationAccountInformation":{},"paymentSourceInformation":{},"amountPaid":78000,"totalPayable":78000,"offlineProductInformation":{"code":"41470","type":"DYNAMIC"},"cardDetails":{},"paymentMethod":"CASH","currency":"NGN","settlementAmount":77600,"paymentStatus":"PAID","customer":{"name":"Mockaroo Jesse","email":"111222333@ZZAMZ4WT4Y3E.monnify"}},"eventType":"SUCCESSFUL_TRANSACTION"}'
hash = 'f04fb635e04d71648bd3cc7999003da6861483342c856d05ddfa9b2dafacb873b0de1d0f8f67405d0010b4348b721c49fa171d317972618debba6b638aedcd3c'

clientSecretRequstBody = clientSecret + requestBody
a = computeSha512(b'91MUDL9N6U3BQRXBQ2PJ9M0PW4J22M1Y',b'{"eventData":{"product":{"reference":"111222333","type":"OFFLINE_PAYMENT_AGENT"},"transactionReference":"MNFY|76|20211117154810|000001","paymentReference":"0.01462001097368737","paidOn":"17/11/2021 3:48:10 PM","paymentDescription":"Mockaroo Jesse","metaData":{},"destinationAccountInformation":{},"paymentSourceInformation":{},"amountPaid":78000,"totalPayable":78000,"offlineProductInformation":{"code":"41470","type":"DYNAMIC"},"cardDetails":{},"paymentMethod":"CASH","currency":"NGN","settlementAmount":77600,"paymentStatus":"PAID","customer":{"name":"Mockaroo Jesse","email":"111222333@ZZAMZ4WT4Y3E.monnify"}},"eventType":"SUCCESSFUL_TRANSACTION"}')
print(a)
print(str(a) == hash)

print('f04fb635e04d71648bd3cc7999003da6861483342c856d05ddfa9b2dafacb873b0de1d0f8f67405d0010b4348b721c49fa171d317972618debba6b638aedcd3c' == hash)