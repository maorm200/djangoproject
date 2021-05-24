from django.shortcuts import render
# Render function needs templates so 
# We are using HttpResponse as it builds the response object that views are expected to return
from django.http import Http404
from .models import Pet # we want to use Pet models to make queries

def home(request):
    pets = Pet.objects.all()
    # Render needs to use templates. We will make all queries here in the views and pass it onto the template.
    return render(request, 'home.html', {
        'pets': pets
    })

# this request is passed pet_id as keyword argument
# so we will use it as a second argument
def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id) # We want to get specific pet with the pet_id that gets passed to here from the urls.py config
    except Pet.DoesNotExist:
        #We want to raise a 404 error if page isn't found
        raise Http404('Pet not found') #will show 404 page with pet not found written there
    # if no errors then render that certain pet
    return render(request, 'pet_detail.html', {
        'pet': pet
    })

