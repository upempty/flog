from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
# Create your views here.
from rest.models import FeeItem
from rest.models import Article
from rest.models import User
from rest.permissions import IsAdminUserOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token

from rest_framework import permissions, pagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


import json
import base64
import time
from django.contrib.auth.hashers import check_password, make_password

class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body for user register: ", body)
        item = json.loads(body)
        name = item.get('username')
        pwd = item.get('password')
        email = item.get('email')
        user = User.objects.filter(username=name)
        if user:
            print('user exists')
            return JsonResponse({'data': [], 'msg': 'failed to register, name exists', 'status': 200})
        else:
            # Forbidden: /post/article/
            #User.objects.create_user(username=name, password=pwd)
            # to create super user for admin permission
            User.objects.create_superuser(username=name, password=pwd, email=email)
            user = User.objects.get(username=name)
            Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=user)

            userinfo = {
                'token': token.key,
                'username': user.username,
            }
            items = [userinfo]
            result = {'data': items, 'msg': 'succeed to register', 'status': 200}
            return JsonResponse(result)


class LoginView(View):
    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body for user login: ", body)
        item = json.loads(body)
        name = item.get('username')
        pwd = item.get('password')
        user = User.objects.filter(username=name)
        if user:
            print('user exists')
            check_pwd = check_password(pwd, user[0].password)
            if check_pwd:
                user = User.objects.get(username=name)
                Token.objects.get_or_create(user=user)
                token = Token.objects.get(user=user)
            else:
               return JsonResponse({'data': [], 'msg': 'failed to login, password wrong', 'status': 200})
        else:
            print('user not exist')
            return JsonResponse({'data': [], 'msg': 'failed to login, username wrong', 'status': 200})

        userinfo = {
            'token': token.key,
            'username': user.username,
        }
        items = [userinfo]
        result = {'data': items, 'msg': 'succeed to login', 'status': 200}
        return JsonResponse(result)


class ArticleAPIView(APIView):

    #ok one permission_classes = [IsAdminUser,]
    #nok authentication_classes = (TokenAuthentication,)
    #permission_classes = (AllowAny,)
    #permission_classes = (IsAdminUser,)
    #permission_classes = (IsAuthenticated, )
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication,]

    def get(self, request, *args, **kwargs):
        title = request.GET.get('title')
        print('title:', title)
        items = []
        if title:
            items = Article.objects.filter(title__icontains=title)
        else:
            items = Article.objects.all() 
        data_values = []
        for i in items:
            each = {'title': i.title, 'description': i.description, 'content': i.content}
            data_values.append(each)
        result = {'data': data_values, 'msg': 'query', 'status': 200} 
        print('result: ', result)
        #return Response(result, json_dumps_params={"ensure_ascii": False})
        return Response(result)

    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        host = 'http://150.158.168.151:9000/'
        #img = request.POST.get('img')
        bb = request.body.decode()
        bb = json.loads(bb)
        #bb = request.POST
        img = bb.get('img')
        print('APIView---')
        '''
        body = request.body.decode()
        item = json.loads(body)
        img = item.get('img')
        '''
        '''
        img = request.POST.get('img')
        '''
        if img is not None:
            print('img ok')
            #img = json.loads(img)
            #img = json.dumps(img)
            print (img)

            img_url = img['url']
            img_name = img['name']
            img_url_list = img_url.split(',')
            img_data = base64.b64decode(img_url_list[1])
            image_name = int(round(time.time() * 1000))
            img_url = 'media/img' + '/' + str(image_name) + '-' + img_name
            with open(img_url, 'wb') as f:
                f.write(img_data)
            u = host + img_url
            result = {'data': u, 'msg': 'create', 'status': 200}
            return Response(result)
        else:
            print('img emtpy')
        #body = request.body.decode()
        #body = request.data.decode()
        #body = request.data
        #body = request.data
        #bb = json.loads(bb)
        body = bb
        print("body: ", body)

        item = body
        #payid = item.get('payid')
        #ret = FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
        ret = Article.objects.create(**item)
        print('ret: ', ret)
        items = [item]
        result = {'data': items, 'msg': 'create', 'status': 200}
        return Response(result)

    def put(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'update', 'status': 200}
        '''
        body = request.body.decode()
        print("put body: ", body)
        item = json.loads(body)
        title = item.get('title')
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        ret = Article.objects.filter(title=title).update(**item)
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'update', 'status': 200}
        return Response(result)

    def delete(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'delete', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        title = item.get('title')
        ret = Article.objects.filter(title=title).delete()
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'delete', 'status': 200}
        return Response(result)



class ArticleView(View):
    def get(self, request, *args, **kwargs):
        title = request.GET.get('title')
        print('title:', title)
        items = []
        if title:
            items = Article.objects.filter(title__icontains=title)
        else:
            items = Article.objects.all() 
        data_values = []
        for i in items:
            each = {'title': i.title, 'description': i.description, 'content': i.content}
            data_values.append(each)
        result = {'data': data_values, 'msg': 'query', 'status': 200} 
        print('result: ', result)
        return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        host = 'http://150.158.168.151:9000/'
        img = request.POST.get('img')
        '''
        body = request.body.decode()
        item = json.loads(body)
        img = item.get('img')
        '''
        '''
        img = request.POST.get('img')
        '''
        if img is not None:
            print('img ok')
            img = json.loads(img)
            img_url = img['url']
            img_name = img['name']
            img_url_list = img_url.split(',')
            img_data = base64.b64decode(img_url_list[1])
            image_name = int(round(time.time() * 1000))
            img_url = 'media/img' + '/' + str(image_name) + '-' + img_name
            with open(img_url, 'wb') as f:
                f.write(img_data)
            u = host + img_url
            result = {'data': u, 'msg': 'create', 'status': 200}
            return JsonResponse(result)
        else:
            print('img emtpy')
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        #payid = item.get('payid')
        #ret = FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
        ret = Article.objects.create(**item)
        print('ret: ', ret)
        items = [item]
        result = {'data': items, 'msg': 'create', 'status': 200}
        return JsonResponse(result)

    def put(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'update', 'status': 200}
        '''
        body = request.body.decode()
        print("put body: ", body)
        item = json.loads(body)
        title = item.get('title')
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        ret = Article.objects.filter(title=title).update(**item)
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'update', 'status': 200}
        return JsonResponse(result)

    def delete(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'delete', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        title = item.get('title')
        ret = Article.objects.filter(title=title).delete()
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'delete', 'status': 200}
        return JsonResponse(result)

class DecorationCartView(View):
    def get(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'query', 'status': 200}
        '''
        name = request.GET.get('name')
        print('naming:', name)
        items = []
        if name:
            items = FeeItem.objects.filter(name__icontains=name)
        else:
            items = FeeItem.objects.all() 
        data_values = []
        for i in items:
            each = {'payid': i.payid, 'name': i.name, 'fee': i.fee, 'paydate': i.paydate}
            data_values.append(each)
        result = {'data': data_values, 'msg': 'query', 'status': 200} 
        #print('result: ', result)
        return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body) 
        item = json.loads(body)
        #payid = item.get('payid')
        #ret = FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
        ret = FeeItem.objects.create(**item)
        print('ret: ', ret) 
        
        items = [item]
        result = {'data': items, 'msg': 'create', 'status': 200}
        return JsonResponse(result)

    def put(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'update', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        name = item.get('name')
        payid = item.get('payid')
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        ret = 0
        if payid is None:
            ret = FeeItem.objects.filter(name=name).update(**item)
        else:
            ret = FeeItem.objects.filter(payid=payid).update(**item)
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'update', 'status': 200}
        return JsonResponse(result)
    
    def delete(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'delete', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        name = item.get('name')
        ret = FeeItem.objects.filter(name=name).delete()
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'delete', 'status': 200}
        return JsonResponse(result)

class FirstView(View):
    def get(self, request, *args, **kwargs):
        #result = {'status': True, 'data': 'first response'}
        '''
        items = [{'id': 8, 'name': '燃气热水器', 'fee': 1, 'paydate': '2020-11-11'},
                 {'id': 8, 'name': '燃气热水器', 'fee': 1, 'paydate': '2020-11-11'}]
        '''
        its = FeeItem.objects.all()
        li = []
        for i in its:
            one = {'payid': i.payid, 'name': i.name, 'fee': i.fee, 'paydate': i.paydate}
            li.append(one)
        result = {'data': li, 'status':200}
        # 'meta': {'status': 200, 'msg': 'no error'}        
        return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        data = request.body.decode()
        dic_data = json.loads(data)
        print("post received", dic_data)
        payid = dic_data.get('payid')
        name = dic_data.get('name')
        fee = dic_data.get('fee')
        paydate = dic_data.get('paydate')
        print(paydate,'paydate')        
        
        if name is None or payid is None:
            result = {'status': 400, 'data':'no data', 'msg': 'ERROR'}
            return JsonResponse(result, json_dumps_params={"ensure_ascii": False})
        else:
            f = FeeItem.objects.filter(name=name)
            if f:
                result = {'status': 401, 'data':'already data', 'msg': 'already'}
                return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

            FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
            items = [dic_data]
            result = {'data': items, 'status': 200, 'msg':'new'}
            print('create ok')
            return JsonResponse(result, json_dumps_params={"ensure_ascii": False})
        return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

    def put(self, request, *args, **kwargs):
        #FeeItem.objects.filter(payid=1).update(payid=payid, name=name)
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        pass

    def delete(self, request, *args, **kwargs):
        #FeeItem.objects.filter(payid=1).delete()
        pass
