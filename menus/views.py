from django.shortcuts import render
from datetime import datetime
from menus.models import Menu

# Create your views here.
def index(request): #render함수는 request와 템플릿이 필수
    date = datetime.now().date()
    data = Menu.objects.all()
    context = {"today":date}
    context["menus"] = data
    return render(request,'menus/index.html',context=context) #템플릿으로 대신 html을 렌더링

def detail(request, pk):
    data = Menu.objects.all()
    context = {}
    for food in data:
        if food.id == pk:
            context["name"] = food.name
            context["name_eng"] = food.name_eng
            context["description"] = food.description
            context["price"] = food.price
            context["img_path"] = food.img_path
            break
    return render(request,'menus/detail.html',context= context)