from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
# Create your views here.
from rest.models import FeeItem
from rest.models import Article
import json
from django.contrib.auth.hashers import check_password, make_password

class Login(View):
    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        name = item.get('username')
        pwd = item.get('password')
        '''
        user = models.User.objects.filter(username=username)
        if user:
            check_pwd = check_password(password, user[0].password)
            if check_pwd:
                user = models.User.objects.get(username=username)
                Token.objects.get_or_create(user=user)
                token = Token.objects.get(user=user)
            else:
               return JsonResponse({})
        else:
            return Response({})

        userinfo = {
            'token': token.key,
            'username': user.username,
        }
        #payid = item.get('payid')
        #ret = FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
        items = [userinfo]
        '''
        items = []
        result = {'data': items, 'msg': 'login', 'status': 200}
        return JsonResponse(result)


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
