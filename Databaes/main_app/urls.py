from django.urls import path
from . import views
from .views import schedule_appointment

#from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name='index'),
    path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
    path('pets/<int:pet_id>/schedule_appointment/', schedule_appointment, name='schedule_appointment'),
    path('pets/<int:pet_id>/delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('pets/<int:pet_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('pests/<int:pet_id>/adopt', views.adopt_pet, name='adopt_pet'),
]