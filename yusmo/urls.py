"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# urls.py
# from rest_framework.routers import DefaultRouter
# from yusmouser.admin_views import NetworkViewSet, AirtimeViewSet, DataViewSet, CableViewSet, CablePlanViewSet, ElectricityViewSet, RechargeCardPlanViewSet, DataCouponViewSet

# router = DefaultRouter()
# router.register(r'networks', NetworkViewSet)
# router.register(r'airtime', AirtimeViewSet)
# router.register(r'data', DataViewSet)
# router.register(r'cables', CableViewSet)
# router.register(r'cableplans', CablePlanViewSet)
# router.register(r'electricity', ElectricityViewSet)
# router.register(r'rechargecardplans', RechargeCardPlanViewSet)
# router.register(r'datacoupons', DataCouponViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yusmouser.urls')),
    # path('', include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
    # path('accounts_allauth/', include('allauth.urls')),
]
