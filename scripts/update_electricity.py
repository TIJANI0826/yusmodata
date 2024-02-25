# import os
# import django

# # Set up Django environment
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
# django.setup()

from yusmouser.models import Electricity

data = [
    {"DiscoID": 1, "DiscoName": "Ikeja Electric"},
    {"DiscoID": 2, "DiscoName": "Eko Electric"},
    {"DiscoID": 3, "DiscoName": "Abuja Electric"},
    {"DiscoID": 4, "DiscoName": "Kano Electric"},
    {"DiscoID": 5, "DiscoName": "Enugu Electric"},
    {"DiscoID": 6, "DiscoName": "Port Harcourt Electric"},
    {"DiscoID": 7, "DiscoName": "Ibadan Electric"},
    {"DiscoID": 8, "DiscoName": "Kaduna Electric"},
    {"DiscoID": 9, "DiscoName": "Jos Electric"},
    {"DiscoID": 11, "DiscoName": "Yola Electric"},
    {"DiscoID": 10, "DiscoName": "Benin Electric"},
]

def run(): 
  # Update or create records in the database
  for entry in data:
      disco_id = entry["DiscoID"]
      disco_name = entry["DiscoName"]
  
      # Try to get an existing record based on disco_id
      electricity_object, created = Electricity.objects.get_or_create(disco_id=disco_id)
  
      # Update the record with the new disco_name
      electricity_object.disco_name = disco_name
      electricity_object.save()
  
      if created:
          print(f"Created new record for DiscoID {disco_id}")
      else:
          print(f"Updated record for DiscoID {disco_id}")
  