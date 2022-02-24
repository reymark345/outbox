from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views




urlpatterns = [
    
    path('',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('createtask/',views.createtask, name='createtask'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)