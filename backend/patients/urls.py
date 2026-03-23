from django.urls import path
from .views import register_patient, search_patient

urlpatterns={
    path('register/', register_patient),
    path('search/' , search_patient),
}