from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item


def home(request):
    return render(request, 'home.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        category = request.POST.get('category')
        size = request.POST.get('size')
        price = request.POST.get('item_price')

        Item.objects.create(
            item_name=item_name,
            category=category,
            size=size,
            price=price
        )
        return redirect('item_list')
    
    return render(request, 'add_item.html')

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.item_name = request.POST.get('item_name')
        item.category = request.POST.get('category')
        item.size = request.POST.get('size')
        item.price = request.POST.get('price')
        item.save()
        return redirect('item_list')

    return render(request, 'items_edit_item.html', {'item': item})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('item_list')

