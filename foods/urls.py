"""rohstaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views #현재디렉토리내에있는 views를 가져와라

urlpatterns = [
    path('menu/', views.index), #views모델에서 index를 가져와라
    path('', views.index),
    path('menu/<int:pk>/', views.food_detail) #동적 url. menu뒤에 오는 url을
    #동적으로 봐서 str으로 변환. 이것을 food_detail에 나중에 인수로 줄거임.


]
