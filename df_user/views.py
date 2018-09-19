import json,copy
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from hashlib import sha1
from .models import UserInfo
# Create your views here.
from boke.httpResponData import httpResponData

#用户注册
def register(request):
    response_data = copy.deepcopy(httpResponData)
    if request.method == "GET":
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        username = request.POST.get('name')
        paw = request.POST.get('paw')
        cpaw = request.POST.get('cpaw')
        email = request.POST.get('email')


        #判断当前用户是否注册过
        count = UserInfo.objects.filter(username=username).exists()
        if count:
            response_data['remark'] = "该用户已注册"
            return HttpResponse(json.dumps(response_data),content_type="application/json")

        #判断密码是否一致
        if paw !=cpaw:
            response_data['remark'] = "秘密不一致"
            return HttpResponse(json.dumps(response_data),content_type="application/json")

        #密码加密
        s1 = sha1()
        s1.update(paw.encode('utf-8'))
        paw3 = s1.hexdigest()

        #创建对象
        user = UserInfo()
        user.username = username
        user.password = paw3
        user.useremail = email
        user.save()
        response_data['result'] = True
        response_data['remark'] = "注册成功"

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

        username = request.POST.get('name')
        password = request.POST.get('paw')

        #根据用户名查对象
        user = UserInfo.objects.filter(username=username)

        if len(user)==1:
            pass
            s1 = sha1()
            s1.update(password.encode('utf-8'))
            if s1.hexdigest() == user[0].password:
                print("验证通过")    #记住密码前端实现
                request.session['user_id']  = user[0].id
                request.session['username']  = username

                response_data['result'] = True
            else:
                pass
        else:
            pass
            response_data['remark'] = "用户名不存在"

        return HttpResponse(json.dumps(response_data),content_type="application/json")

