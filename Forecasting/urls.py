
from django.urls import path
from . import views
urlpatterns =[
path('',views.Forecasting, name='Forecasting'),
path('',views.result)




]






