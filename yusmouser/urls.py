from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
app_name = "yusmouser"

urlpatterns = [
  path("", views.homepage, name="homepage"),
  path("register", views.register, name="register"),
  path("login", views.sign_in, name="login"),
  path('logout', views.sign_out, name='logout'),
  path('buydata', views.buydata, name='buydata'),
  path('buyairtime', views.buyairtime, name='buyairtime'),
  path('buyelectricity', views.buyelectricity, name='buyelectricity'),
  path('resultchecker', views.result_checker, name='resultchecker'),
  path('buycable', views.buycable, name='buycable'),
  path('fund_wallet', views.fund_wallet, name='fund_wallet'),
  path('fund_wallet2',views.fund_wallet2,name='fund_wallet2'),
  path('data_transanction',views.data_transanction,name='data_transanction'),
  path('airtime_transanction',views.airtime_transanction,name='airtime_transanction'),
  path('wallet_finding',views.wallet_finding,name='wallet_finding'),
  #path('electricity_transanction',views.electricity_transanction,name='electricity_transanction'),
  path('print_recharge_card',views.print_recharge_card,name='print_recharge_card'),
  path('mtn_data_pin',views.mtn_data_pin,name='mtn_data_pin'),
  path('monnify/webhook_payment',views.webhook_payment,name='webhook_payment'),
  path('paystack/webhook',views.webhook_paystack_payment,name='webhook_paystack_payment'),
  path('uic_number',views.get_uic_number,name='get_uic_number'),
  path('get_meter',views.get_meter,name='get_meter'),
]
from  . import admin_urls
urlpatterns += admin_urls.urlpatterns
