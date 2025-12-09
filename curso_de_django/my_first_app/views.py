from django.shortcuts import render
from .models import Car

# Create your views here.
def my_view(request):
    
    car_list = Car.objects.all()

    return render(request, 'my_first_app/car_list.html', {"car_list_key": car_list})