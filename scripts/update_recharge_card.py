import json
from yusmouser.models import Recharge_Card_Plan

# Assuming your JSON data is stored in a variable named 'data'

recharge_cards = [
    {
      "RechargeID": 1,
      "RechargeNetwork": "MTN",
      "Amount": 100.0
    },
    {
      "RechargeID": 2,
      "RechargeNetwork": "MTN",
      "Amount": 200.0
    },
    {
      "RechargeID": 3,
      "RechargeNetwork": "MTN",
      "Amount": 500.0
    },
    {
      "RechargeID": 4,
      "RechargeNetwork": "MTN",
      "Amount": 1000.0
    },
    {
      "RechargeID": 5,
      "RechargeNetwork": "AIRTEL",
      "Amount": 100.0
    },
    {
      "RechargeID": 6,
      "RechargeNetwork": "AIRTEL",
      "Amount": 200.0
    },
    {
      "RechargeID": 7,
      "RechargeNetwork": "AIRTEL",
      "Amount": 500.0
    },
    {
      "RechargeID": 8,
      "RechargeNetwork": "AIRTEL",
      "Amount": 1000.0
    },
    {
      "RechargeID": 9,
      "RechargeNetwork": "GLO",
      "Amount": 100.0
    },
    {
      "RechargeID": 10,
      "RechargeNetwork": "GLO",
      "Amount": 200.0
    },
    {
      "RechargeID": 11,
      "RechargeNetwork": "GLO",
      "Amount": 500.0
    },
    {
      "RechargeID": 12,
      "RechargeNetwork": "GLO",
      "Amount": 1000.0
    }
  ]

def run():
  # Loop through the data and create Recharge_Card_Plan instances
  for card_data in recharge_cards:
      Recharge_Card_Plan.objects.create(
          recharge_id=card_data["RechargeID"],
          recharge_network_name=card_data["RechargeNetwork"],
          amount=card_data["Amount"]
      )
  