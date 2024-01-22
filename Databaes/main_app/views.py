from django.shortcuts import redirect, render

# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Pet

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