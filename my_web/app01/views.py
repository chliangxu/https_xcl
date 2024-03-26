from django.shortcuts import render
from django.http import HttpResponse
from app01.models import select_computer_info
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def select_machine(requests):
    if requests.method == 'GET':
        datas = select_computer_info()
        print(type(datas), datas)
        if datas:
            return render(requests, 'newdb.html', {"data": datas})
        else:
            return render(requests, 'wait.html')
