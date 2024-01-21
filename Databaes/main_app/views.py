from django.shortcuts import redirect, render

# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Dog

#dummy data
# dogs = [
#     {'name': 'Snoopy', 'species': 'Dog', 'size': 'Small', 'age': 2, 'gender': 'M'},
#     {'name': 'Doggo', 'specees': 'Dog', 'size': 'Large', 'age': 10, 'gender': 'F'},
#     {'name': 'Ash', 'species': 'Dog', 'size': 'Medium', 'age': 5, 'gender': 'F'},
# ]

# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')
def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

#define dogs index view
def dogs_index(request):
    dogs = Dog.objects.all()
    return render (request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog': dog })

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