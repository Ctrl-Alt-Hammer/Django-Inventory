from django.shortcuts import render, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from . import forms


# Grabs all items in inventory_list and displays them in decending order.
def inventory_list(request):
    inventorys = Inventory.objects.all().order_by('-created_at')
    return render(request, 'inventory/inventory_list.html', {'inventorys': inventorys})

def inventory_page(request, slug):
    inventory = Inventory.objects.get(slug=slug)
    return render(request, 'inventory/inventory_page.html', {'inventory': inventory})  

@login_required(login_url='/users/login/')
def new_item(request):
    if request.method == 'POST':
       form = forms.CreateInventory(request.POST, request.FILES)
       if form.is_valid():
           new_item = form.save(commit=False)
           new_item.author = request.user
           new_item.save()
           return redirect('inventory:list')
    else:
        form = forms.CreateInventory()
    return render(request, 'inventory/add_new_item.html', {'form': form})