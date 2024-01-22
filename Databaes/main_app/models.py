from django.db import models
# from django.urls import reverse
from django.urls import reverse

# Import the User
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    # size = models.CharField(max_length=100)
    age = models.IntegerField()
    # gender = models.CharField(max_length=100)
    shots_received = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    fixed = models.BooleanField(default=False)

    # Add the foreign key linking to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"