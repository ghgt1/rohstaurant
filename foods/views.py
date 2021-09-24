from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import Menu
# Create your views here.
# view는 request가 들어왔을때 응답을하는 모델

def index(request): #render함수는 request와 템플릿이 필수
    context={}
    today = datetime.today().date() #로직을 담당하는 vies에서 템플릿으로 동적 정보 넘겨줌
    menus = Menu.objects.all() # DB에서 모든 음식가져오기
    context["date"] = today
    context["menus"] = menus
    return render(request,'foods/index.html',context = context) #템플릿으로 대신 html을 렌더링
# render함수의 세번째 parameter == context에 dictionary형태로 넘겨줘야함



def food_detail(request, pk):
    #항상 템플릿으로 넘겨주는건 dictionary로
    context = {}
    menus = Menu.objects.all()
    for food in menus:
        if food.id==pk:
            context["name"] = food.name
            context["description"] = food.description
            context["price"] = food.price
            context["img_path"] = food.img_path
            break
    return render(request,'foods/detail.html',context=context)