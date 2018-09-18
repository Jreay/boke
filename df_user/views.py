import json,copy
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from boke.httpResponData import httpResponData

#用户注册
def register(request):
    response_data = copy.deepcopy(httpResponData)
    if request.method == "GET":
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        response_data['result'] = True
        response_data['data'] = {
            "a":request.POST.get('name'),
            "b":request.POST.get('paw')
        }
        return HttpResponse(json.dumps(response_data),content_type="application/json")




#用户登录
def loginin(request):
    response_data = copy.deepcopy(httpResponData)
    if request.method == "GET":
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        response_data['result'] = True
        response_data['data'] = {
            "a":request.POST.get('name'),
            "b":request.POST.get('paw')
        }
        return HttpResponse(json.dumps(response_data),content_type="application/json")

