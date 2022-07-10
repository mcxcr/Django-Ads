"""mazorka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include

# from two_factor.urls import urlpatterns as tf_urls

# Next 2 lines enable Admin OTP Feature - 2F Module
# from two_factor.admin import AdminSiteOTPRequired
# admin.site.__class__ = AdminSiteOTPRequired

# Next 2 lines enable Admin OTP Feature - Original
SERVER_ENV_IS = int(os.environ.get('SERVER_ENV_IS')) == 1

if not SERVER_ENV_IS:
    from django_otp.admin import OTPAdminSite
    admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(tf_urls)),
]
