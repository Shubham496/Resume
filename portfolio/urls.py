from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('',                  views.landing,         name='landing'),
    path('resume/',           views.resume,          name='resume'),
    path('projects/',         views.projects_list,   name='projects_list'),
    path('projects/<slug:slug>/', views.project_detail,  name='project_detail'),
    path('contact/',          views.contact,         name='contact'),
]
