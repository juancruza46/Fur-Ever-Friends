from django.urls import path
from . import views

#from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name= 'index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    #path('accounts/signup/', views.signup, name='signup'),
]