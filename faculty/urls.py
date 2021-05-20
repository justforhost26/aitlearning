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
from django.urls import path

from faculty import views


urlpatterns = [
    path('Home/',views.home,name="home"),
    path('Add_Video/', views.add_video, name="add_video"),
    path('Profile/', views.profile, name="profile"),
    path('Logout/', views.logout, name="logout"),
    path('Edit/<id>', views.edit, name="edit"),
path('update_Profile/<id>', views.update_profile, name="update_profile"),
path('Update_Profile_Pic/<id>', views.update_profile_pic, name="update_profile_pic"),
path('do_Update_Profile_Pic/<id>', views.do_update_profile_pic, name="do_update_profile_pic"),
path('Update_Password/<id>', views.update_password, name="update_password"),
path('do_Update_password/<id>', views.do_update_password, name="do_update_password"),
path('Do_Add_Video/', views.do_add_video, name="do_add_video"),
path('Delete_Video/<id>', views.delete_video, name="delete_video"),
path('Edit_Video/<id>', views.edit_video, name="edit_video"),
path('Do_Edit_Video/<id>', views.do_edit_video, name="do_edit_video"),
path('Contact/', views.contact_faculty, name="contact_faculty"),
path('Contact_us/', views.contact_us, name="contact_us"),
path('Search/', views.search, name="search"),

]
