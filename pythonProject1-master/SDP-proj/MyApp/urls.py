from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.initial, name = 'inital'),
    path("home",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("vehicles", views.vehicles, name= "vehicles"),
    path("vehicles1", views.vehicles1, name= "vehicles1"),
    path("vehicles2", views.vehicles2, name= "vehicles2"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
    path("bill",views.order,name = "bill"),
    path("bill1",views.order1,name = "bill1"),
    path("bill2",views.order2,name = "bill2"),
    path("contact",views.contact,name = 'contact'),

    ]