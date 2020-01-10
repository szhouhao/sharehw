from    django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from sharehw.models import *

import uuid

def index(request):
    print('hello')
    return render(request, 'list.html')


class DocView(APIView):
    pass