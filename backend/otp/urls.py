from django.urls import path
from .views import *

urlpatterns=[
    path('send/',send_otp),
    path('verify/', verify_otp),
]