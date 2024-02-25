import requests
import json
import os

HUSMODATA_TOKEN = "5880b91337684eb36e97f1b67be852b9bcec9d85"

BASE_URL = 'https://www.husmodataapi.com/api'
def buyAirtimeVTU(network_id, amount, mobile_number, airtime_type):
    url = f"{BASE_URL}/topup/"

    payload = json.dumps({
        "network": network_id,
        "amount": amount,
        "mobile_number": mobile_number,
        "Ported_number": "false",
        "airtime_type": airtime_type
    })
    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def buyData(network_id, mobile_number, plan_id):

    url = f"{BASE_URL}/data/"

    payload = json.dumps({
        "network": network_id,
        "mobile_number": mobile_number,
        "plan": plan_id,
        "Ported_number": 'false'
    })
    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def buyElectricityBill(disco, amount, meter_number, meter_type_id):
    url = f"{BASE_URL}/billpayment/"

    payload = json.dumps({
        "disco_name": disco,
        "amount": amount,
        "meter_number": meter_number,
        "meter_type_id": meter_type_id
    })

    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def cableSub(cablename, cableplan_id, smart_card_number):
    url = f"{BASE_URL}/cablesub/"

    payload = json.dumps({
        "cablename": cablename,
        "cableplan": cableplan_id,
        "smart_card_number": smart_card_number
    })

    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def getAllDataTransaction():
    url = f"{BASE_URL}/data/"

    payload = ""
    headers = {'Authorization': 'Token {}'.format(HUSMODATA_TOKEN), '': ''}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def queryDataTransaction(id):
    url = f"{BASE_URL}/data/"

    payload = json.dumps({"id": id})
    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def queryAirtimeTransaction(id):
    url = f"{BASE_URL}/data"

    payload = ""
    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def queryBillTransaction(id):
    url = f"{BASE_URL}/billpayment/{id}"

    payload = ""
    headers = {'Authorization': 'Token {}'.format(HUSMODATA_TOKEN)}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def queryCableTransaction():
    url = f"{BASE_URL}/cablesub/id"

    payload = ""
    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def validateIUC(smart_card,cable_company):
  url = f"{BASE_URL}/validateiuc?smart_card_number={smart_card}&cablename={cable_company}"
  payload = ""
  headers = {
  'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
  'Content-Type': 'application/json'
}
  response = requests.request("GET", url, headers=headers, data=payload)
  return response.json()
  
def validateMeterNumber(meter_number, disco_name, meter_type_id):
    url = f"{BASE_URL}/validatemeter?meternumber={meter_number}&disconame={disco_name}&mtype={meter_type_id}"

    payload = ""
    headers = {
        'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def buyMTNGiftingCoupon(data_plan,quantity,name_on_card):

  url = f"{BASE_URL}/datarechargepin/"

  payload = json.dumps({
      "data_plan": data_plan,
      "quantity": quantity,
      "name_on_card": name_on_card,
  })

  # payload = "{\r\n    \"data_plan\": \"\",\r\n    \"quantity\": \"1\",\r\n    \"name_on_card\": \"\"\r\n}"
  headers = {
    'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.json()
def buyResultChecker(exam_name,quantity):

  url = f"{BASE_URL}/epin/"

  payload = json.dumps({
      "exam_name": exam_name,
      "quantity": quantity,
  })

  headers = {
    'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.json()
def generateRechargeCard(network,network_amount,quantity,name_on_card):

  url = f"{BASE_URL}/rechargepin/"
  payload =json.dumps({
                         "network": network,
                         "network_amount": network_amount,
                         "quantity": quantity,
                         "name_on_card":name_on_card
  })
  headers = {
    'Authorization': 'Token {}'.format(HUSMODATA_TOKEN),
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.json()

def airtime_to_cash(network,mobile_number,amount):
  import requests

  url = f"{BASE_URL}/Airtime_funding/"
  payload =json.dumps({
                         "network": network,
                         "mobile_number": mobile_number,
                         "amount": amount,
  })
  # payload = "{\n    \"network\":network, //query \"/api/get/network/\"  to get all available networks, and their ID\n    \"mobile_number\": mobile_number,\n    \"amount\": amount\n}"
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.json()
#print(validateIUC("2021949493","GOTV"))
#print(buyAirtimeVTU(1, 50, '09134349252', "VTU"))
#print(buyData(1, '08141994147', 51))
#print(queryDataTransaction('1'))
# print(buyElectricityBill(13, 2000, 1234567890, 1))
# print(generateRechargeCard(1,1,1,'TJTECH'))