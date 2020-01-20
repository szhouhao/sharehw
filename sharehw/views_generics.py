from rest_framework import generics
from django.db.models import Q
from    django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from sharehw.utils.public.api_class import APIActionClass
from sharehw.utils.public.response_utils import json_response
from sharehw.utils.public.errno_utils import *
from sharehw.utils.cal import *
class CalManage(APIView):
    def __init__(self):
        self.username='zhouhao'
    api=APIActionClass(
        get_api={'getcal':'get_cal'},
        post_api={}
    )
    def get(self, request, action):
        try:
            self.api.cls = CalAPI(request, self.username)
            result = self.api.get_func(action)()
        except Exception as e:
            return json_response(ServiceStatusCode.REQUEST_ERROR, msg=str(e))
        else:
            return json_response(ServiceStatusCode.REQUEST_SUCCESS, data=result)

    def post(self, request, action):
        try:
            self.api.cls = CalAPI(request, self.username)
            self.api.post_func(action)()
        except Exception as e:
            return json_response(ServiceStatusCode.REQUEST_ERROR, msg=str(e))
        else:
            return json_response(ServiceStatusCode.REQUEST_SUCCESS)