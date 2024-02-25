import json
import os
import requests
import base64
from datetime import date, datetime


PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_LIVE_SECRET_KEY')
# PAYSTACK_SECRET_KEY = 'sk_live_ed5adf0fef92b2067a3ad76255ce5c1a51f7c6a4'
BASE_URL = "https://api.paystack.co"


def create_customer(email = "zero@sum.com", first_name = "Zero", last_name = "Sum", phone = "+2348123456789"):
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(PAYSTACK_SECRET_KEY)
  }
  
  data=json.dumps({ 
    "email": email,
    "first_name": first_name,
    "last_name": last_name,
    "phone": phone
  })
  url = f'{BASE_URL}/customer'
  res = requests.request("POST",url=url,headers=headers,data=data)
  return res.json()

def customer_details(email_or_code):
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(PAYSTACK_SECRET_KEY)
  }
  
  url = f'{BASE_URL}/customer/{email_or_code}'
  res = requests.request("GET",url=url,headers=headers)
  return res.json()

def create_dedicated_virtual_account(email = "janedoe@test.com", first_name = "Jane", middle_name = "Karen", last_name = "Doe", phone = "+2348100000000", preferred_bank = "test-bank", country = "NG"):
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(PAYSTACK_SECRET_KEY)
  }
  
  data=json.dumps({ 
    "email": email,
    "first_name": first_name,
    "middle_name": middle_name,
    "last_name": last_name,
    "phone": phone,
    "preferred_bank": preferred_bank,
    "country": country
  })
  url = f'{BASE_URL}/dedicated_account'
  res = requests.request("POST",url=url,headers=headers,data=data)
  return res.json()



def assign_dedicated_virtual_account(customer,preferred_bank):
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(PAYSTACK_SECRET_KEY)
  }
  
  data=json.dumps({ 
    "customer": customer, 
    "preferred_bank":preferred_bank
  })
  url = f'{BASE_URL}/dedicated_account'
  res = requests.request("POST",url=url,headers=headers,data=data)
  return res.json()
  
def initialize_transaction(email,amount):
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(PAYSTACK_SECRET_KEY)
  }
  
  data=json.dumps({ 
    "email": email,
    "amount": amount
  })
  url = f'{BASE_URL}/transaction/initialize'
  res = requests.request("POST",url=url,headers=headers,data=data)
  return res.json()

def verify_transaction(reference):
  headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(PAYSTACK_SECRET_KEY)
  }
  
  url = f'{BASE_URL}/transaction/verify/{reference}'
  res = requests.request("GET",url=url,headers=headers)
  return res.json()

# print(create_dedicated_virtual_account("tijanibrahim24@gmail.com","Jane","Karen","Doe","+2348141994147", "wema-bank","NG"))
# print(create_customer("zero@sum.com","Zero", "Sum","+2348123456789"))
print(assign_dedicated_virtual_account("zero@sum.com","wema-bank"))
# print(customer_details('zero@sum.com'))