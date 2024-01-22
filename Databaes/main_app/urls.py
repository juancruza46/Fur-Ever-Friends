from django.urls import path
from . import views

#from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name= 'index'),
    path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    #path('accounts/signup/', views.signup, name='signup'),
]