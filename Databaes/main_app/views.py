from django.shortcuts import render

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

