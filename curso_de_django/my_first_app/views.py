from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
from django.views.generic.base import TemplateView

# Create your views here.
def my_view(request):
    
    return render(request, 
                  'my_first_app/car_list.html', 
                  {"car_list_key": Car.objects.all()})

class CarListView(TemplateView):
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self):
        context  = {"car_list_key": Car.objects.all()}
        return context



def example_view(request):
    return HttpResponse("Hello, this is the example view.")

def my_dinamic_view(request, *args, **kwargs):
    id = kwargs.get('id')
    print(args)
    print(kwargs)
    return HttpResponse(f"This is a dynamic view with id: {id}")