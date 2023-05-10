
from django.shortcuts import render, get_object_or_404
from .models import Car,Part
from users.models import profile
from django.http import HttpResponse
import uuid
from .utils import searchcars, paginatevehicles,paginatepart
from urllib.parse import urlencode

""""""

def car_listing(request):
    allvehicles , model, type = searchcars(request)
    custom_range, allvehicles = paginatevehicles(request, allvehicles,6)
    context = {
        'allvehicles': allvehicles,
        'type':type,
        'model':model,
        'custom_range':custom_range
    }
    return render(request, 'cars/cars.html', context)

   
def onecar(request, pk):
    viewcar = Car.objects.select_related('dealer').get(id=pk)
    message = f"I'm interested in buying the car/spareparts from your website  . Could you please provide more information?"
    mobile = viewcar.dealer.phone_number # Replace with dynamic mobile number
    params = {'text': message, 'phone': mobile}
    whatsapp_url = f"https://wa.me/{mobile}?{urlencode(params)}"
    context = {
        'viewcar': viewcar,
        'whatsapp_url': whatsapp_url,
    }
    return render(request, 'cars/single-car.html', context)
 
def part_list(request):
    parts = searchcars(request)
    custom_range, parts = paginatepart(request, parts,6)
    query = request.GET.get('q')


    


    if query:
        custom_range, parts = paginatepart(request, parts,6)
        parts = Part.objects.filter(name__icontains=query)
    else:
        parts = Part.objects.all()
        custom_range, parts = paginatepart(request, parts,6)
    context = {
        'parts': parts,
        'query': query,
    }
    return render(request, 'parts/parts.html',context)


    
def part_detail(request, part_id):
    part = Part.objects.select_related('dealer').get(pk=part_id)
    context = {'part': part}
    return render(request, 'parts/part_detail.html', context)
