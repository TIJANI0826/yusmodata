# serializers.py
from rest_framework import serializers
from .models import network, Airtime, Data, Cable, CablePlan, Electricity, Recharge_Card_Plan, Data_Coupon

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = network
        fields = '__all__'

class AirtimeSerializer(serializers.ModelSerializer):
    network = NetworkSerializer()

    class Meta:
        model = Airtime
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class CableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cable
        fields = '__all__'

class CablePlanSerializer(serializers.ModelSerializer):
    cable = CableSerializer()

    class Meta:
        model = CablePlan
        fields = '__all__'

class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Electricity
        fields = '__all__'

class RechargeCardPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recharge_Card_Plan
        fields = '__all__'

class DataCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_Coupon
        fields = '__all__'
