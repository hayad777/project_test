from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list, name='member_list'),
    path('programs/', views.program_list, name='program_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sports/', views.sports, name='sports'),
    path('contact/', views.contact_us, name='contact_us'),
    path('', views.home, name='home'),


]
