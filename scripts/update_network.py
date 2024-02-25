# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name' with the actual name of your Django project

# import django
# django.setup()

from yusmouser.models import network  # Replace 'your_app_name' with the actual name of your Django app

networks = [{
    "NetworkID": 1,
    "NetworkName": "MTN",
}, {
    "NetworkID": 2,
    "NetworkName": "GLO",
}, {
    "NetworkID": 3,
    "NetworkName": "9MOBILE",
}, {
    "NetworkID": 4,
    "NetworkName": "AIRTEL",
}]


def run():
    for network_data in networks:
        network_id = network_data["NetworkID"]
        network_name = network_data["NetworkName"]

        # Try to get an existing network with the given ID
        existing_network = network.objects.filter(
            network_id=network_id).first()

        if existing_network:
            # Update the existing network
            existing_network.network_name = network_name
            existing_network.save()
            print(f"Updated network with ID {network_id}")
        else:
            # Create a new network if it doesn't exist
            new_network = network(network_id=network_id,
                                  network_name=network_name)
            new_network.save()
            print(f"Created network with ID {network_id}")
