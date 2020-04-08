from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('example/', views.example, name='example'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.sign_up, name="signup"),
]