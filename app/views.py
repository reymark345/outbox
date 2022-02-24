from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth, Permission
from django.contrib.sessions.models import Session
from django.http import JsonResponse,HttpResponse
from datetime import date
import json
from .models import task_tbl


def login(request):
    return render(request, 'login.html')

def dashboard(request):
    tasks = task_tbl.objects.all()
    tasks = {'requestsdata':tasks}
    return render(request, 'dashboard.html',tasks)

def createtask(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        # category1 = request.POST.get('cat1')

        createRequest = task_tbl.objects.create(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            date_requested = date.today()
            # category1 = request.POST.get('cat1'),
            # date_upload = datetime.date.today()
		)
        # category2 = request.POST.get('cat2')
        print("hoissss");
        return JsonResponse({'data': 'success'})
