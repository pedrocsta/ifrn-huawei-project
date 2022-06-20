from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # SOBRE
    path('about/ict-academy/', views.ict_academy, name='ict-academy'),
    path('about/huawei/', views.huawei, name='huawei'),
    #

    # CURSOS
    path('courses/5g-networks/', views.cincoG_networks, name='5g-networks'),
    path('courses/artificial-intelligence/', views.artificial_intelligence, name='artificial-intelligence'),
    path('courses/cloud-service/', views.cloud_service, name='cloud-service'),
    path('courses/datacom/', views.datacom, name='datacom'),
    # 

    # EVENTOS
    path('events/ict-competition-brasil/', views.ict_competition_brasil, name='ict-competition-brasil'),
    path('events/ict-job-fair-brasil/', views.ict_job_fair_brasil, name='ict-job-fair-brasil'),
    path('events/seeds-for-the-future/', views.seeds_fot_the_future, name='seeds-for-the-future'),
    # 
    
    path('laboratories/', views.laboratories, name='laboratories'),
    path('instructors/', views.instructors, name='instructors'),
    path('certification/', views.certification, name='certification'),
    path('contact/', views.contact, name='contact'),
]
