from django.urls import path
from . import views

urlpatterns = [
    path('graph/dashboard',views.dashboard, name='dashboard'),
]
