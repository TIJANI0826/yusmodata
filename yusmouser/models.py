from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    accountReference = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_account_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_wallet_balance = models.DecimalField(default=0.00,decimal_places=2,max_digits=13)
  
class MonnifyTransaction(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  transactionRefrence = models.CharField(max_length = 1000)
  paymentReference = models.CharField(max_length = 1000)
  amountPaid = models.CharField(max_length = 1000)
  totalPayable = models.CharField(max_length = 1000)
  settlementAmount = models.CharField(max_length = 1000)
  paidOn = models.CharField(max_length = 1000)
  paymentStatus = models.CharField(max_length = 1000)
  paymentDescription = models.CharField(max_length = 1000)
  currency = models.CharField(max_length = 1000)
  paymentMethod = models.CharField(max_length = 1000)

class DataTransaction(models.Model):
  customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  transaction_id = models.CharField(max_length = 200)
  ident = models.CharField(max_length = 200)
  balance_before = models.CharField(max_length = 200)
  balance_after = models.CharField(max_length = 200)
  mobile_number = models.CharField(max_length = 200)
  status = models.CharField(max_length = 200)
  plan_network = models.CharField(max_length = 200) 
  plan_name  = models.CharField(max_length = 200)
  plan_amount =  models.CharField(max_length = 200)
  create_date = models.DateField(auto_now_add=True)
  ported_number = models.CharField(max_length = 200)
  api_response =  models.CharField(max_length = 2000)
  


class AirtimeTransaction(models.Model):
  customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  transaction_id = models.CharField(max_length = 200)
  ident = models.CharField(max_length = 200)
  mobile_number = models.CharField(max_length = 200)
  status = models.CharField (max_length = 200)
  plan_network = models.CharField(max_length = 200) 
  airtime_type  = models.CharField(max_length = 200)
  paid_amount =  models.CharField(max_length = 200)
  balance_before = models.CharField(max_length = 200)
  balance_after = models.CharField(max_length = 200)
  create_date = models.DateField(auto_now_add=True)
  ported_number = models.CharField(max_length = 200)
  api_response =  models.CharField(max_length = 2000)
  customer_ref = models.CharField(max_length = 2000)

AIRTIME_TYPE = [
    ("Share and Sell", "Share and Sell"),
    ("VTU", "VTU"),
]

class network(models.Model):
  network_id = models.CharField(max_length = 200)
  network_name = models.CharField(max_length = 200)
  def __str__(self):
    return self.network_name
class Airtime(models.Model):
  network = models.ForeignKey(network, on_delete=models.DO_NOTHING)
  airtime_type = models.CharField(max_length=15, choices=AIRTIME_TYPE, default='1')
  def __str__(self):
    return self.network.network_name

class Data(models.Model):
  data_id = models.CharField(max_length  = 200) 
  network	= models.CharField(max_length = 200)
  plan_type = models.CharField(max_length = 200)
  amount	= models.CharField(max_length = 200)
  size	= models.CharField(max_length = 200)
  validity = models.CharField(max_length = 200)
  def __str__(self):
    return self.data_id

class Cable(models.Model):
  cable_id = models.CharField(max_length = 200)
  cable_name = models.CharField(max_length = 200)
  def __str__(self):
    return self.cable_name
  
class CablePlan(models.Model):
  cable = models.ForeignKey(Cable, on_delete=models.DO_NOTHING)
  cableplan_id =  models.CharField(max_length = 200)
  cable_plan_name = models.CharField(max_length = 200)
  cableplan_amount = models.CharField(max_length = 200)
  def __str__ (self):
    return self.cable_plan_name

class Electricity(models.Model):
  disco_id	= models.CharField(max_length = 200)
  disco_name = models.CharField(max_length = 200)
  def __str__(self):
    return self.disco_name
    
class Recharge_Card_Plan(models.Model):
  recharge_id	= models.CharField(max_length = 200)
  recharge_network_name	= models.CharField(max_length = 200)
  amount = models.CharField(max_length = 200)
  def __str__(self):
    return self.recharge_id
class Data_Coupon(models.Model):
  data_coupon_id = models.CharField(max_length = 200)
  data_coupon_network_name = models.CharField(max_length = 200)
  amount = models.CharField(max_length = 200)
  def __str__(self):
    return self.data_coupon_id