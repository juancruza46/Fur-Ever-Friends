from django.shortcuts import redirect, render
import uuid, boto3, os



# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet, Photo


#dummy data
# pets = [
#     {'name': 'Snoopy', 'species': 'Pet', 'size': 'Small', 'age': 2, 'gender': 'M'},
#     {'name': 'go', 'specees': 'Pet', 'size': 'Large', 'age': 10, 'gender': 'F'},
#     {'name': 'Ash', 'species': 'Pet', 'size': 'Medium', 'age': 5, 'gender': 'F'},
# ]

# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')
def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

#define pets index view
def pets_index(request):
    pets = Pet.objects.all()
    return render (request, 'pets/index.html', {'pets': pets})

def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', { 'pet': pet })

class PetCreate(CreateView):
    model = Pet
    fields = ['name', 'species', 'age', 'shots_received', 'description', 'fixed']
    success_url = '/pets/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    #template_name = 'pets/pet_form.html'

class PetUpdate(UpdateView):
    model = Pet
    #exclude what you dont want to be able to edit after creation
    fields = ['name', 'species', 'age', 'shots_received', 'description', 'fixed']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/pets'

def add_photo(request, pet_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, pet_id=pet_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
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