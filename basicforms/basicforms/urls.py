"""basicforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from basicapp import views
from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    #path('formpage/',views.form_name_view,name='form_name'),
    path('user/',views.users,name='users'),
    path('data/',views.official_data,name='data'),
    path('table/',views.new_user_table,name='req'),
    path('check/',views.check1,name='chk'),
    path('goto/',views.search,name='chk'),
    path('research/',views.research,name='chk'),
    path('rtable/',views.research_table,name='chk'),
    path('reached/',views.note,name='chk'),
    path('gotonotif/',views.update_n,name='chk'),
    url('app/', include('basicapp.urls')),
]
