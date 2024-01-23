from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Pet, Photo, Appointment
from .forms import AppointmentForm
import uuid
import boto3
import os

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pets_index(request):
    pets = Pet.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

def pets_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    appointments = pet.appointments.all()  # Get all appointments related to the pet

    return render(request, 'pets/detail.html', {'pet': pet, 'appointments': appointments})

class PetCreate(CreateView):
    model = Pet
    fields = ['name', 'species', 'age', 'shots_received', 'description', 'fixed']
    success_url = '/pets'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return redirect('offerta_create',args=(self.object.id,))

class PetUpdate(UpdateView):
    model = Pet
    fields = ['name', 'species', 'age', 'shots_received', 'description', 'fixed']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/pets'

def add_photo(request, pet_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        upload_photo_to_s3(photo_file, pet_id)
    return redirect('detail', pet_id=pet_id)

def upload_photo_to_s3(photo_file, pet_id):
    s3 = boto3.client('s3')
    key = f"{uuid.uuid4().hex[:6]}{photo_file.name[photo_file.name.rfind('.'):]}"

    try:
        bucket = os.environ['S3_BUCKET']
        s3.upload_fileobj(photo_file, bucket, key)
        url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
        Photo.objects.create(url=url, pet_id=pet_id)
    except Exception as e:
        print('An error occurred uploading file to S3')
        print(e)

@login_required
def schedule_appointment(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.pet = pet
            appointment.save()
            return redirect('detail', pet_id=pet_id)
    else:
        form = AppointmentForm()

    return render(request, 'pets/detail.html', {'form': form, 'pet': pet})

def delete_appointment(request, pet_id, appointment_id):
    # Retrieve the appointment
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the user has permission to delete the appointment (optional)
    if request.user == appointment.pet.user:
        # Delete the appointment
        appointment.delete()

    # Redirect back to the pet detail page
    return redirect('detail', pet_id=pet_id)




# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#         # This will add the user to the database
#             user = form.save()
#             # This is how we log a user in via code
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = 'Invalid sign up - try again'
#             # A bad POST or a GET request, so render signup.html with an empty form
#         form = UserCreationForm()
#         context = {'form': form, 'error_message': error_message}
#         return render(request, 'registration/signup.html', context)