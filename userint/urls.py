from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('entry/', views.entryPage, name = "entry"),
    path('thankyou/', views.thankyouPage, name = "thankyou"),
    path('tooearly/', views.tooearlyPage, name = "tooearly"),
    path('toolate/', views.toolatePage, name = "toolate"),
    path('ceeessvee/', views.extract_CSV, name = "ceeessvee"),
]