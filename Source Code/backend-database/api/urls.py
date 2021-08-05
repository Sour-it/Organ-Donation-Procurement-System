from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.get_client),
    path('nclient/', views.new_client),
    path('job/', views.get_job),
    path('comp/', views.get_comp),
    path('ins/', views.get_insurance),
    path('nstaff/', views.put_staff),
    path('pstaff/', views.get_staff),
    path('proc/', views.new_procurement),
    path('bill/', views.get_bill),
    path('organs/', views.organ),
    path('oavail/', views.avail),
    path('grec/', views.get_rep),
    path('gdon/', views.get_don),
    path('staff/', views.get_staffs)
]
