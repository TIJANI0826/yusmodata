import hashlib
import hmac
import os
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse

from django.contrib import messages
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

import datetime
from .models import Customer, DataTransaction, AirtimeTransaction, MonnifyTransaction
from .network import get_network, create_network, update_network, delete_network
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from .models import network, Airtime, Data, Cable, CablePlan, Electricity, Recharge_Card_Plan, Data_Coupon
from .serializers import NetworkSerializer, AirtimeSerializer, DataSerializer, CableSerializer, CablePlanSerializer, ElectricitySerializer, RechargeCardPlanSerializer, DataCouponSerializer

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

def dashboard(request):
  User = get_user_model()
  users = User.objects.all()
  users_count = users.count()
  today_user_count = User.objects.filter(last_login__startswith=timezone.now().date()).count()
  current_users = get_current_users()
  return render(request, 'admin/admin_dashboard.html',{"users" : users, "users_count":users_count, "today_user_count" : today_user_count, "current_users" : current_users})

def admin_airtime(request):
  return render(request, 'admin/admin_airtime.html')
def admin_airtime2cash(request):
  return render(request, 'admin/admin_airtime2cash.html')
def admin_cable(request):
  cables = Cable.objects.all()
  return render(request, 'admin/admin_cable.html',{"data_plans" : data_plans})
def admin_datacardplans(request):
  return render(request, 'admin/admin_datacardplans.html')
def admin_dataplan(request):
  data_plans = Data.objects.all()
  return render(request, 'admin/admin_dataplan.html', {"data_plans" : data_plans})
def admin_education(request):
  return render(request, 'admin/admin_education.html')
def admin_electricity(request):
  return render(request, 'admin/admin_electricity.html')
def admin_rechargepins(request):
  return render(request, 'admin/admin_rechargepins.html')

# views.py
class NetworkViewSet(viewsets.ModelViewSet):
    queryset = network.objects.all()
    serializer_class = NetworkSerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in network._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset
     
    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in network._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)
                            
class AirtimeViewSet(viewsets.ModelViewSet):
    queryset = Airtime.objects.all()
    serializer_class = AirtimeSerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in Airtime._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset

    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in Airtime._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in Data._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset

    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in Data._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class CableViewSet(viewsets.ModelViewSet):
    queryset = Cable.objects.all()
    serializer_class = CableSerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in Cable._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset

    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in Cable._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class CablePlanViewSet(viewsets.ModelViewSet):
    queryset = CablePlan.objects.all()
    serializer_class = CablePlanSerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in CablePlan._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset

    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in CablePlan._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class ElectricityViewSet(viewsets.ModelViewSet):
    queryset = Electricity.objects.all()
    serializer_class = ElectricitySerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in Electricity._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset

    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in Electricity._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class RechargeCardPlanViewSet(viewsets.ModelViewSet):
  queryset = Recharge_Card_Plan.objects.all()
  serializer_class = RechargeCardPlanSerializer
  http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

  def get_queryset(self):
    queryset = self.queryset
    params = self.request.query_params
    for field in Recharge_Card_Plan._meta.get_fields():
      if field.name in params:
        queryset = queryset.filter(**{field.name: params[field.name]})
    return queryset

  def destroy(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    filter_kwargs = {}
    for field in Recharge_Card_Plan._meta.get_fields():
      if field in kwargs:
        filter_kwargs[field] = kwargs[field]
    queryset = queryset.filter(**filter_kwargs)
    instance = queryset.first()
    if instance is not None:
      self.perform_destroy(instance)
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)

class DataCouponViewSet(viewsets.ModelViewSet):
    queryset = Data_Coupon.objects.all()
    serializer_class = DataCouponSerializer
    http_method_names = ['get', 'post','put', 'patch', 'head', 'options', 'trace','delete']

    def get_queryset(self):
      queryset = self.queryset
      params = self.request.query_params
      for field in Data_Coupon._meta.get_fields():
        if field.name in params:
          queryset = queryset.filter(**{field.name: params[field.name]})
      return queryset

    def destroy(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      filter_kwargs = {}
      for field in Data_Coupon._meta.get_fields():
        if field in kwargs:
          filter_kwargs[field] = kwargs[field]
      queryset = queryset.filter(**filter_kwargs)
      instance = queryset.first()
      if instance is not None:
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)



# class NetworkListCreateView(generics.ListCreateAPIView):
#     queryset = network.objects.all()
#     serializer_class = NetworkSerializer

# class AirtimeListCreateView(generics.ListCreateAPIView):
#     queryset = Airtime.objects.all()
#     serializer_class = AirtimeSerializer

# class DataListCreateView(generics.ListCreateAPIView):
#     queryset = Data.objects.all()
#     serializer_class = DataSerializer

# # Add other views similarly
# class CableListCreateView(generics.ListCreateAPIView):
#     queryset = Cable.objects.all()
#     serializer_class = CableSerializer

# class CablePlanListCreateView(generics.ListCreateAPIView):
#     queryset = CablePlan.objects.all()
#     serializer_class = CablePlanSerializer
# class ElectricityListCreateView(generics.ListCreateAPIView):
#     queryset = Electricity.objects.all()
#     serializer_class = ElectricitySerializer

# class RechargeCardPlanListCreateView(generics.ListCreateAPIView):
#     queryset = Recharge_Card_Plan.objects.all()
#     serializer_class = RechargeCardPlanSerializer
# class DataCouponListCreateView(generics.ListCreateAPIView):
#     queryset = Data_Coupon.objects.all()
#     serializer_class = DataCouponSerializer

