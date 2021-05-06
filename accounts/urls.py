from django.urls import path
from . import views
urlpatterns =[


path('register',views.register, name='register'),
path('login',views.login, name='login'),
path('admin_login',views.admin_login, name='admin_login'),
path('Finalarea/',views.Finalarea, name='finalarea'),
path('table',views.table, name='table'),
path('graph/dashboard',views.dashboard, name='dashboard'),
path('admin_dashboard',views.admin_dashboard, name='admin_dashboard'),
path('showusers',views.showusers, name='showusers')









]