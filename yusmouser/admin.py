from django.contrib import admin
from .models import Customer,DataTransaction,AirtimeTransaction,MonnifyTransaction,network,Airtime,Cable,CablePlan,Data,Electricity,Recharge_Card_Plan,Data_Coupon
# Register your models here.
admin.site.register(Customer)
admin.site.register(DataTransaction)
admin.site.register(AirtimeTransaction)
admin.site.register(MonnifyTransaction)
admin.site.register(network)
admin.site.register(Airtime)
admin.site.register(Cable)
admin.site.register(CablePlan)
admin.site.register(Data)
admin.site.register(Electricity)
admin.site.register(Recharge_Card_Plan)
admin.site.register(Data_Coupon)