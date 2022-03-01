from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth, Permission
from django.contrib.sessions.models import Session
from django.http import JsonResponse,HttpResponse
from datetime import date
import json
from .models import card_tbl, gallery_photos
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, 'login.html')

def dashboard(request):
    card = card_tbl.objects.all()
    card = {'requestsdata':card}
    return render(request, 'dashboard.html',card)

def taskboard(request):
    card = card_tbl.objects.all()
    card = {'requestsdata':card}
    return render(request, 'dashboard.html',card)

@csrf_exempt
def createtask(request):
    if request.method == 'POST':
        # urgent = request.POST.get('resultData')
        cat1 = request.POST.get('cat1')
        cat2 = request.POST.get('cat2')
        cat2 = (int(cat2))
        cat2 = cat2 - 3
        createRequest = card_tbl.objects.create(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            date_requested = date.today(),
            category1_id = cat1,
            category2_id = cat2
		)
        for file in request.FILES.getlist('photos[]'):
            oas = gallery_photos.objects.create(
                card_id = createRequest.id,
                photos =  file,
			)
        return JsonResponse({'data': 'success'})

@csrf_exempt
def updateStatus(request):
    if request.method=="POST":
        cardId = request.POST.get('id')
        source = request.POST.get("sources")
        target = request.POST.get('targets')

        card_tbl.objects.filter(id=cardId).update(status=target)
        return JsonResponse({'datas': 'test'})

@csrf_exempt
def viewCard(request):
    if request.method=="POST":
        card = card_tbl.objects.all()
        card = {'data':"test"}

        print("halaka")
        return JsonResponse(card)

