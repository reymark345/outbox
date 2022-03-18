from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth, Permission
from django.contrib.sessions.models import Session
from django.http import JsonResponse,HttpResponse
from datetime import date
import json
from .models import card_tbl, gallery_photos, category1_tbl
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db import connection


def login(request):
    return render(request, 'login.html')

def dashboard(request):
    card = card_tbl.objects.all()
    card = {'requestsdata':card}
    print("one")
    return render(request, 'dashboard.html',card)

def taskboard(request):
    card = card_tbl.objects.all()
    card = {'requestsdata':card}
    print("test")
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

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@csrf_exempt
def viewCard(request):
    if request.method=="POST":
        cardId = request.POST.get('id')
        image = gallery_photos.objects.filter(id = cardId)
        print("test")
        print(image)
        with connection.cursor() as cursor:
            cursor.execute("SELECT act.id,act.title,act.description,act.requested_by,act1.name AS cat1name,act2.name AS cat2name,agp.photos,prt.name AS levels FROM app_card_tbl AS act INNER JOIN app_category1_tbl AS act1 ON act1.id = act.category1_id INNER JOIN app_category2_tbl AS act2 ON act2.id = act.category2_id INNER JOIN app_gallery_photos AS agp ON agp.card_id = act.id INNER JOIN app_priority_tbl AS prt ON prt.id = act2.priority_id WHERE act.id =%s", [cardId])
            query = dictfetchall(cursor)
            print("test")
            print(query)
        card = {'data':query}
        return JsonResponse(card)

