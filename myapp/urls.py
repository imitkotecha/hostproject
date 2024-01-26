from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('profile/',views.profile),
    path('notes/',views.notes,name='notes'),
    path('contact/',views.contact),
    path('userlogout/',views.userlogout),
   

]