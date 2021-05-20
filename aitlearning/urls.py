"""aitlearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from aitlearning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
path('About',views.about,name="about"),
path('Contact',views.contact,name="contact"),
path('Faculty',views.faculty,name="faculty"),
    path('faculty_login',views.faculty_login,name="faculty_login"),
    path('faculty_register',views.faculty_register,name="faculty_register" ),
    path('do_faculty_login', views.do_faculty_login, name="do_faculty_login"),
    path('do_faculty_register', views.do_faculty_register, name="do_faculty_register"),
    path('Verify_Otp', views.verify_otp, name="verify_otp"),
    path('faculty/', include('faculty.urls')),
path('Contact/', views.contact_us, name="contact_us"),
path('search_main/', views.search_main, name="search_main"),

]

