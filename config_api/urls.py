from django.urls import path
from .views import *

urlpatterns = [
    path('production-info/', ProductionInfo.as_view(), name='production-info'),
]