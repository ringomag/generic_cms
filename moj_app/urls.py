
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('o_sajtu/', views.o_sajtu, name = 'o_sajtu'),
    path('kontakt/', views.kontakt, name = 'kontakt'),
]
