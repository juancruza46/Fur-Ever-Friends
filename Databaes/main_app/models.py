from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#-----------------------------------------------------------#
# Pet Model:
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    shots_received = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    fixed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})
#-----------------------------------------------------------#
# Photo Model:    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"
    
#-----------------------------------------------------------#
# Appointment model:
class Appointment(models.Model):
    date = models.DateField('Appointment Date')
    time = models.TimeField('Appointment Time')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return f"{self.pet.name}'s Appointment on {self.date} at {self.time}"

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})