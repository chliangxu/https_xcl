from django.shortcuts import render
from django.http import HttpResponse
from app01.models import select_computer_info
import datetime
# Create your views here.

def index(request):
    time = datetime.datetime.now()
    txt = f"现在是{time} <br>"
    txt += "hello world"
    return HttpResponse(txt)

def select_machine(requests):
    if requests.method == 'GET':
        datas = select_computer_info()
        print(type(datas), datas)
        if datas:
            return render(requests, 'newdb.html', {"data": datas})
        else:
            return render(requests, 'wait.html')
