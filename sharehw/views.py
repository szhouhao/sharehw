from    django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from sharehw.models import *

import uuid

def index(request):
    print('hello')
    return render(request, 'index.html')
def matain(request):
    return render(request, 'matain.html')

class DocView(APIView):
    pass

