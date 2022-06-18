from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # SOBRE
    # 

    # CURSOS
    # 

    # EVENTOS
    # 
    
    path('laboratories/', views.laboratories, name='laboratories'),
    path('instructors/', views.instructors, name='instructors'),
    path('certification/', views.certification, name='certification'),
    path('contact/', views.contact, name='contact'),
]
