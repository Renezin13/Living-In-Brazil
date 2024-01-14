from django.contrib import admin
from django.urls import path, include
from app_LIB.views import *

urlpatterns = [
    path('', home, name='home'),
    path('pontos_turisticos/', pontos_turisticos, name='pontos_turisticos'),
    path('login/', login, name='login'),
    path('pontos_turisticos/<int:id>/', pt_descricao, name='pt_descricao')
]