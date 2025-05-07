from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.

def index_view(requests):
    return render(requests, template_name="index.html")


def PictureID_view(request, Picture_id):
    Picture_id = int(Picture_id)

    return HttpResponse(f"现在的图片ID是{Picture_id}")


def info_view(requests):
    username = "大大怪"
    military_rank = "将军"

    xiashu_dic = {
        "name": "小小怪",
        "military_rank": "下士",
    }

    context = {"username": username, "military_rank": military_rank, "xiashu_dic": xiashu_dic}

    return render(requests, template_name="info.html", context=context)

def url_view(requests):

    return render(requests, template_name="url.html")

def filter_view(requests):

    green = "Hello World"

    context = {
        "green": green,
        "birthday": datetime.now(),
        "profile": ""
    }
    return render(requests, template_name="filter.html", context=context)

def template_view(requests):

    context = {
        "articles": ["小米suv7", "开心超人" ]
    }
    return render(requests, template_name="xfz_index.html", context=context)

def static_view(requests):

    return render(requests, template_name="static.html")