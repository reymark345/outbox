from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views




urlpatterns = [
    
    path('',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('createtask/',views.createtask, name='createtask'),
    path('taskboard/',views.taskboard, name='taskboard'),
    path('updateStatus/',views.updateStatus, name='updateStatus'),
    path('viewCard/',views.viewCard, name='viewCard'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)