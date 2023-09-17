from core.views import index,contact
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('signup/',views.SignUp, name='signup'),
    

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)