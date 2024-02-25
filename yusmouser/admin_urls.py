from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
# from .admin_views import dashboard, NetworkListCreateView, AirtimeListCreateView, DataListCreateView
from .admin_views import dashboard, NetworkViewSet, AirtimeViewSet, DataViewSet, CableViewSet, CablePlanViewSet, ElectricityViewSet, RechargeCardPlanViewSet, DataCouponViewSet,admin_airtime,admin_airtime2cash,admin_cable,admin_dataplan,admin_electricity,admin_rechargepins,admin_datacardplans,admin_electricity,admin_education
# hgh
router = DefaultRouter()
router.register(r'networks', NetworkViewSet)
router.register(r'airtime', AirtimeViewSet)
router.register(r'data', DataViewSet)
router.register(r'cables', CableViewSet)
router.register(r'cable-plans', CablePlanViewSet)
router.register(r'electricity', ElectricityViewSet)
router.register(r'recharge-card-plans', RechargeCardPlanViewSet)
router.register(r'data-coupons', DataCouponViewSet)
urlpatterns = [
  path('admin_airtime',admin_airtime,name="admin_airtime"),
  path('admin_airtime2cash',admin_airtime2cash,name="admin_airtime2cash"),
  path('admin_cable',admin_cable,name="admin_cable"),
  path('admin_dataplan',admin_dataplan,name="admin_dataplan"),
  path('admin_rechargepins',admin_rechargepins,name="admin_rechargepins"),
  path('admin_datacardplans',admin_datacardplans,name="admin_datacardplans"),
  path('admin_electricity',admin_electricity,name="admin_electricity"),
  path('admin_education',admin_education,name="admin_education"),
  path('fastadmin',dashboard,name="yusmo_admin_dashboard"),
  path('network/', NetworkViewSet.as_view({'get': 'list','post' : 'create',
                                          'put': 'update',
                                          'patch': 'partial_update',
                                          'delete': 'destroy'},name= 'network_list')),
  path('network/<int:pk>/', NetworkViewSet.as_view({ 'get': 'list',
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'}), name='network-list-create'),

  path('data/', DataViewSet.as_view({'get': 'list','post' : 'create'},name= 'data_list')),
  path('data/<int:pk>/', DataViewSet.as_view({
  'get': 'retrieve',
  'put': 'update','patch': 'partial_update',
  'delete': 'destroy'}), name='data-list-create'),

  path('airtime/', AirtimeViewSet.as_view({'get': 'list','post' : 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'},name= 'airtime_list')),
  path('airtime/<int:pk>/', AirtimeViewSet.as_view({ 'get': 'list',
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'}), name='airtime-list-create'),

  path('cable/', CableViewSet.as_view({'get': 'list','post' : 'create',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'},name= 'cable_list')),
  path('cable/<int:pk>/', CableViewSet.as_view({ 'get': 'list',
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'}), name='cable-list-create'),

  path('cableplan/', CablePlanViewSet.as_view({'get': 'list','post' : 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'},name= 'cableplan_list')),
  path('cableplan/<int:pk>/', CablePlanViewSet.as_view({ 'get': 'list',
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'}), name='cableplan-list-create'),

  path('rechargecardplan/', RechargeCardPlanViewSet.as_view({'get': 'list','post' : 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'},name= 'rechargecardplan_list')),
  path('rechargecardplan/<int:pk>/', RechargeCardPlanViewSet.as_view({ 'get': 'list',
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'}), name='rechargecardplan-list-create'),

  path('electricity/', ElectricityViewSet.as_view({'get': 'list','post' : 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'},name= 'electricity_list')),
  path('electricity/<int:pk>/', ElectricityViewSet.as_view({ 'get': 'list',
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'}), name='electricity-list-create'),

  path('datacoupon/', DataCouponViewSet.as_view({'get': 'list','post' : 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'},name= 'datacoupon_list')),
  path('datacoupon/<int:pk>/', DataCouponViewSet.as_view({ 'get': 'list',
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'}), name='datacoupon-list-create'),
  path('api/', include(router.urls)),
]