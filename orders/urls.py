from django.urls import path
from .import views


urlpatterns = [
   path("",views.Index,name="Index"),
   path('', views.home, name='home'),
   path('menu/', views.menu, name='menu'),
   path('about/', views.about, name='about'),
   path("detail/<int:id>/", views.detail,name="detail"),
   path('contact/', views.contact, name='contact'),
   path('login/',views.loginView,name='login'),
   path('register/',views.register,name='register'),
]




