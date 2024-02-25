import re
import json
from yusmouser.models import Cable, CablePlan

# JSON data
cables = [
  {
    "CableID": 1,
    "CableName": "GOTV"
  },
  {
    "CableID": 2,
    "CableName": "DSTV"
  },
  {
    "CableID": 3,
    "CableName": "STARTIME"
  }
]

cablePlans = [
 {
   "CableplanID": 2,
   "CableplanName": "GOtv Max",
   "CableplanAmount": 4850
 },
 {
   "CableplanID": 6,
   "CableplanName": "DStv Yanga",
   "CableplanAmount": 3500
 },
 {
   "CableplanID": 7,
   "CableplanName": "DStv Compact",
   "CableplanAmount": 10500
 },
 {
   "CableplanID": 8,
   "CableplanName": "DStv Compact Plus",
   "CableplanAmount": 16600
 },
 {
   "CableplanID": 9,
   "CableplanName": "DStv Premium",
   "CableplanAmount": 24500
 },
 {
   "CableplanID": 11,
   "CableplanName": "Classic - 3,800Naira - 1 Mont",
   "CableplanAmount": 3800
 },
 {
   "CableplanID": 12,
   "CableplanName": "Basic - 2,600Naira - 1 Month",
   "CableplanAmount": 2600
 },
 {
   "CableplanID": 13,
   "CableplanName": "Smart - 3,500 Naira - 1 Month",
   "CableplanAmount": 3500
 },
 {
   "CableplanID": 14,
   "CableplanName": "Nova - 1500 Naira - 1 Month",
   "CableplanAmount": 1500
 },
 {
   "CableplanID": 15,
   "CableplanName": "Super - 6500 Naira - 1 Month",
   "CableplanAmount": 6500
 },
 {
   "CableplanID": 16,
   "CableplanName": "GOtv Jinja",
   "CableplanAmount": 2250
 },
 {
   "CableplanID": 17,
   "CableplanName": "GOtv Jolli",
   "CableplanAmount": 3300
 },
 {
   "CableplanID": 19,
   "CableplanName": "DStv Confam",
   "CableplanAmount": 6200
 },
 {
   "CableplanID": 20,
   "CableplanName": "DStv Padi",
   "CableplanAmount": 2500
 },
 {
   "CableplanID": 23,
   "CableplanName": "DStv Asia",
   "CableplanAmount": 8300
 },
 {
   "CableplanID": 24,
   "CableplanName": "DStv Premium French",
   "CableplanAmount": 36600
 },
 {
   "CableplanID": 25,
   "CableplanName": "DStv Premium Asia",
   "CableplanAmount": 32800
 },
 {
   "CableplanID": 29,
   "CableplanName": "DStv Compact + Extra View",
   "CableplanAmount": 13900
 },
 {
   "CableplanID": 30,
   "CableplanName": "DStv Premium + Extra View",
   "CableplanAmount": 27900
 },
 {
   "CableplanID": 31,
   "CableplanName": "DStv Compact Plus - Extra View",
   "CableplanAmount": 20000
 },
 {
   "CableplanID": 34,
   "CableplanName": "GOtv Smallie - Monthly",
   "CableplanAmount": 1100
 },
 {
   "CableplanID": 35,
   "CableplanName": "GOtv Smallie - Quarterly",
   "CableplanAmount": 2900
 },
 {
   "CableplanID": 36,
   "CableplanName": "GOtv Smallie - Yearly",
   "CableplanAmount": 8600
 },
 {
   "CableplanID": 37,
   "CableplanName": "Nova - 500 Naira - 1 Week",
   "CableplanAmount": 500
 },
 {
   "CableplanID": 38,
   "CableplanName": "Basic - 900 Naira - 1 Week",
   "CableplanAmount": 900
 },
 {
   "CableplanID": 39,
   "CableplanName": "Smart - 1100 Naira - 1 Week",
   "CableplanAmount": 1100
 },
 {
   "CableplanID": 40,
   "CableplanName": "Classic - 1500 Naira - 1 Week",
   "CableplanAmount": 1500
 },
 {
   "CableplanID": 41,
   "CableplanName": "Super -2,200 Naira - 1 Week",
   "CableplanAmount": 2200
 },
 {
   "CableplanID": 42,
   "CableplanName": "Nova - 150 Naira - 1 Day",
   "CableplanAmount": 150
 },
 {
   "CableplanID": 43,
   "CableplanName": "Basic - 300 Naira - 1 Day",
   "CableplanAmount": 300
 },
 {
   "CableplanID": 44,
   "CableplanName": "Smart - 350 Naira - 1 Day",
   "CableplanAmount": 350
 },
 {
   "CableplanID": 45,
   "CableplanName": "Classic - 400 Naira - 1 Day",
   "CableplanAmount": 400
 },
 {
   "CableplanID": 46,
   "CableplanName": "Super - 600 Naira - 1 Day",
   "CableplanAmount": 600
 },
 {
   "CableplanID": 47,
   "CableplanName": "GOtv Supa 1 month",
   "CableplanAmount": 6400
 },
 {
   "CableplanID": 48,
   "CableplanName": "Special - 5000 Naira - 1 Month",
   "CableplanAmount": 5000
 },
 {
   "CableplanID": 49,
   "CableplanName": "Special - 1,600 Naira - 1 Week",
   "CableplanAmount": 1600
 },
 {
   "CableplanID": 50,
   "CableplanName": "Special - 500 Naira - 1 Day",
   "CableplanAmount": 500
 },
 {
   "CableplanID": 51,
   "CableplanName": "GOtv Super Plus",
   "CableplanAmount": 10500
 }
]
def run():
  # Update Cable model
  for cable_data in cables:
      cable_id = cable_data["CableID"]
      cable_name = cable_data["CableName"]

      # Update existing or create a new Cable instance
      cable_instance, created = Cable.objects.get_or_create(cable_id=cable_id, defaults={"cable_name": cable_name})

  # Update CablePlan model
  for plan_data in cablePlans:
      cableplan_id = plan_data["CableplanID"]
      cableplan_name = plan_data["CableplanName"]
      cableplan_amount = plan_data["CableplanAmount"]

      # Determine CableID based on CableplanName
      if "GOTV" in cableplan_name.upper():
          cable_id = 1
      elif "DSTV" in cableplan_name.upper():
          cable_id = 2
      else:
          cable_id = 3

      # Get the Cable instance
      cable_instance = Cable.objects.get(cable_id=cable_id)

      # Update existing or create a new CablePlan instance
      plan_instance, created = CablePlan.objects.update_or_create(
          cable=cable_instance,
          cableplan_id=cableplan_id,
          defaults={"cable_plan_name": cableplan_name,"cableplan_amount": cableplan_amount},
      )
