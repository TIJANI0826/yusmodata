import json
from yusmouser.models import Data_Coupon  # Replace 'your_app' with the actual name of your Django app

# Your JSON data
data_coupon = [
    {"Coupon ID": 5, "Data Coupon Network name": "MTN", "amount": 331},
    {"Coupon ID": 6, "Data Coupon Network name": "MTN", "amount": 663},
    {"Coupon ID": 7, "Data Coupon Network name": "MTN", "amount": 1104},
    {"Coupon ID": 8, "Data Coupon Network name": "MTN", "amount": 442},
    {"Coupon ID": 10, "Data Coupon Network name": "MTN", "amount": 166},
    {"Coupon ID": 11, "Data Coupon Network name": "MTN", "amount": 221},
]

def run():
  # Update the Data_Coupon model with the JSON data
  for item in data_coupon:
      data_coupon_obj, created = Data_Coupon.objects.get_or_create(
          data_coupon_id=str(item.get("Coupon ID")),
          data_coupon_network_name=item.get("Data Coupon Network name"),
          amount=str(item.get("amount")),
      )
  
      if not created:
          # Update the existing object if it already exists
          data_coupon_obj.data_coupon_network_name = item.get("Data Coupon Network name")
          data_coupon_obj.amount = str(item.get("amount"))
          data_coupon_obj.save()

  print("Data_Coupon model updated successfully.")
