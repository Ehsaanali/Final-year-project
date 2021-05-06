"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', include('HCMAS.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('graph/epi',include('epi.urls')),
    path('graph/LHW',include('LHW.urls')),
    path('graph/LHW_Areawise',include('LHW_Areawise.urls')),
    path('graph/LHW_ReportsWise',include('LHW_ReportsWise.urls')),
    path('graph/Reports_TB',include('Reports_TB.urls')),
    path('graph/Reports_EPI',include('Reports_EPI.urls')),
    path('graph/Reports_LHW',include('Reports_LHW.urls')),
    path('graph/Trends',include('Trends.urls')),
    path('graph/infant_death',include('infant_death.urls')),
    path('graph/Forecasting',include('Forecasting.urls')),
    path('graph/result',include('Forecasting.urls')),

    

    path('',include('menuapi.urls')),
    path('',include("graph.urls")),
    path('graph/dashboard/Immunizationchart',include("Immunizationchart.urls")),

    
    
    
    
]


