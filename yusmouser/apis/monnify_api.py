import json
import os
import requests
import base64
from datetime import datetime

# from django.conf import settings

MONNIFY_BASE_URL = "https://api.monnify.com"
MONNIFY_API_KEY = "MK_PROD_4RS9EEK7XF"
MONNIFY_SECRET_KEY = "UAP4GU0Z8GG6ANR6AVVCSG9AJJV81D7Q"
MONNIFY_WALLET_ACCOUNT_NUMBER = "8016575571"
MONNIFY_CONTRACT_CODE = "272745166491"

def get_access_token():

    api_tokenSecretToken = MONNIFY_API_KEY + ':' + MONNIFY_SECRET_KEY

    api_tokenSecretToken = base64.b64encode(
        api_tokenSecretToken.encode('ascii'))
    api_tokenSecretToken = api_tokenSecretToken.decode('ascii')

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic {}".format(api_tokenSecretToken)
    }

    login_url = MONNIFY_BASE_URL + "/api/v1/auth/login"

    res_login = requests.request("POST", url=login_url, headers=headers).json()
    access_token = res_login['responseBody']['accessToken']
    return access_token


def create_reserverd_account(accountReference,accountName,customerEmail,customerName,bvn=12345678901):
  data = json.dumps({
        "accountReference": accountReference,
        "accountName": accountName,
        "currencyCode": "NGN",
        "contractCode": MONNIFY_CONTRACT_CODE,
        "customerEmail": customerEmail,
        "bvn": bvn,
        "customerName": customerName,
        "getAllAvailableBanks": "true"
  })
  headers2 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(get_access_token())
  }

  reserve_account_url = MONNIFY_BASE_URL + '/api/v2/bank-transfer/reserved-accounts'
  res2 = requests.request("POST",url=reserve_account_url,headers=headers2,data=data)
  return res2.json()


def get_account_details(accountReference):

    account_details_url = MONNIFY_BASE_URL + '/api/v2/bank-transfer/reserved-accounts/' + accountReference
    headers3 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(get_access_token())
    }

    res3 = requests.request("GET", url=account_details_url, headers=headers3)
    return res3.json()

def get_transaction_status(transactionReference):

    account_details_url = MONNIFY_BASE_URL + '/api/v2/transactions/' + transactionReference
    headers3 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(get_access_token())
    }

    res4 = requests.request("GET", url=account_details_url, headers=headers3)
    return res4.json()
def initate_transaction(amount,customerName,customerEmail,paymentDescription):
  account_details_url = MONNIFY_BASE_URL + '/api/v1/merchant/transactions/init-transaction'
  data = json.dumps({
    "amount": 100.00,
    "customerName": customerName,
    "customerEmail": customerEmail,
    "paymentReference": str(datetime.now),
    "paymentDescription": customerName + customerEmail,
    "currencyCode": "NGN",
    "contractCode": MONNIFY_CONTRACT_CODE,
    "redirectUrl": "https://yusmodata.tjib.repl.co/fund_wallet",
    "paymentMethods":["CARD","ACCOUNT_TRANSFER"]
  })
  
  headers3 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(get_access_token())
  }
  res4 = requests.request("GET", url=account_details_url, headers=headers3)
  return res4.json()
  
    
def get_all_transaction(account_reference ):
  # Set up the headers with API key and secret key
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(get_access_token())
  }
  # API endpoint to get offline payment transactions for a reserved account
  endpoint = f"{MONNIFY_BASE_URL}/api/v1/bank-transfer/reserved-accounts/transactions?accountReference={account_reference}&page=0&size=10"

  # Query parameters
  
  try:
    # Make the GET request to the Monnify API
    response = requests.request("GET", url=endpoint, headers=headers)

    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
      # Parse the JSON response
      data = response.json()
      with open("webhook.txt", "a") as f:
        print(data,file=f)
      # Extract and print the transactions
      transactions = data.get("responseBody")
      return (transactions['content'])
     
    else:
      return f"Error: {response.status_code} - {response.text}"
  
  except Exception as e:
    return f"An error occurred: {str(e)}"

   
# print(get_transaction_status("MNFY|42|20230806160015|103762"))
#print(get_account_details(accountReference="tijanibrahim24tijanibrahim24@gmail.com"))
# print(
#     create_reserverd_account("12345abc", "momodu", "modu@gmail.com", 'momodu'))
# print(get_all_transaction(account_reference="tijanibrahim24tijanibrahim24@gmail.com"))
