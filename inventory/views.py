from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")

def detail(request, item_id):
    return render(request, 'inventory/detail.html', {'item': Item.objects.get(pk=item_id)}) # render detail.html template with item context
