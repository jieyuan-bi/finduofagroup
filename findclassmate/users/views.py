from re import A
from django.shortcuts import render
from django.template import response
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from .models import *
import logging
import os
from django.conf import settings
from django.core.files import File

# Get an instance of a logger
logger = logging.getLogger(__name__)

# returns all the catalogues and subjects
class SignupView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')
        wechat = request.data.get('wechat')
        major = request.data.get('major')
        gender = request.data.get('gender')
        onecard = request.FILES['onecard']
        response={'success':'1'}
        safe_password = encryptPassword(password)
        logger.info('onecard',onecard)
        image_name = onecard.name
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        #create a dir when not exist
        try:
            os.mkdir(settings.MEDIA_ROOT)
        except Exception:
            pass
        #save file to local
        f = open(image_path,'wb')
        for i in onecard.chunks():
            f.write(i)
        f.close()
        # try to create a new registered user
        try:
            UserModel.objects.create(name=name, gender=gender, email=email, major=major, phone=phone, wechat=wechat, 
            password=safe_password,onecard=image_name)
        # if the username already exist, give a flag
        except IntegrityError as e:
            response['success']='-1'
        except Exception as e:
            # logger.info("[Users] Fail to create user!\n", e)
            response['success']='0'
        return Response(response)

class LoginView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        account = request.data.get('account')
        password = request.data.get('password')
        response={'success':1}
        #create admin_account,super super user
        # try:
        #     createAdmin()
        # except Exception:
        #     pass
        try:
            check_password, role = checkPassword(account, password)
        except Exception:
            response['success']=0
            return Response(response)
        # logger.info(check_password )
        if not check_password:
            response['success']=0
        response['role']=role
        return Response(response)

class getUsersView(APIView):
    def get(self, request, *args, **kwargs):
        result = UserModel.objects.all()
        response={}
        response['users']=[]
        for i in result:
            user = {'name':i.name,'gender':i.gender,'phone':i.phone,'wechat':i.wechat,'email':i.email,'onecard':i.get_onecard(),
            'role':i.role,'create_time':i.create_time, 'major':i.major}
            response['users'].append(user)
        return Response(response)

class adminSearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        logger.info('query:', query)
        users = searchUser(query)
        response={}
        response['users']=users
        return Response(response)

class confirmOnecardView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        response={}
        response['success']=0
        #supersuper user cannot change
        # logger.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!name:',name)
        if name=='jieyuan':
            return Response(response)
        try:
            user = UserModel.objects.get(name=name)
            user.role=1
            user.save()
            response['success']=1
        except Exception as e:
            pass
        return Response(response)
