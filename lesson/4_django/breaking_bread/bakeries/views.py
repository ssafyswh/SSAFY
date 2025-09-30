from django.shortcuts import render, get_object_or_404, redirect
from .models import Bakery
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    bakeries = Bakery.objects.all().order_by('rating')

    context = {
        'bakeries': bakeries,
    }

    return render(request, 'bakeries/index.html', context)

def detail(request, id):
    # bakery = Bakery.objects.filter(id=id).first()
    # if bakery is None:
    #     return HttpResponseNotFound("<h1>page not existed</h1>")
    bakery = get_object_or_404(Bakery, id=id)
    context = {
        'bakery': bakery
    }
    return render(request, 'bakeries/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        rating = request.POST.get('rating')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        Bakery.objects.create(
            name=name,
            address=address,
            rating=rating,
            opening_time=opening_time,
            closing_time=closing_time,
        )
        return redirect('bakeries:index')
    else:
        return render(request, 'bakeries/create.html')
    
def delete(request, id):
    bakery = get_object_or_404(Bakery, id=id)
    bakery.delete()
    return redirect('bakeries:index')

def update(request, id):
    bakery = get_object_or_404(Bakery, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        rating = request.POST.get('rating')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        bakery.name = name
        bakery.address = address
        bakery.rating = rating
        bakery.opening_time = opening_time
        bakery.closing_time = closing_time
        bakery.save()
        return redirect('bakeries:detail', bakery.id)
    else:
        context = {
            'bakery': bakery,
        }
        return render(request, 'bakeries/update.html', context)

from django.utils import timezone
import random

def test(request):
    Bakery.objects.create(
        name='test data',
        address='test data',
        rating=round(random.uniform(0.0, 10.0), 1),
        opening_time=timezone.now(),
        closing_time=timezone.now(),
    )
    return redirect('bakeries:index')