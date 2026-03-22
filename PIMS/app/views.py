from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F


# REGISTER
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# DASHBOARD
@login_required
def dashboard(request):
    items = Item.objects.filter(user=request.user)
    low_stock = items.filter(quantity__lte=F('min_quantity'))

    return render(request, 'dashboard.html', {
        'items': items,
        'low_stock': low_stock
    })


# ADD ITEM
@login_required
def add_item(request):
    if request.method == 'POST':
        Item.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            category=request.POST.get('category'),
            quantity=request.POST.get('quantity'),
            min_quantity=request.POST.get('min_quantity'),
            expiry_date=request.POST.get('expiry_date')
        )
        return redirect('dashboard')

    return render(request, 'add_item.html')


# DELETE ITEM
@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id, user=request.user)
    item.delete()
    return redirect('dashboard')


# EDIT ITEM
@login_required
def edit_item(request, id):
    item = get_object_or_404(Item, id=id, user=request.user)

    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.category = request.POST.get('category')
        item.quantity = request.POST.get('quantity')
        item.min_quantity = request.POST.get('min_quantity')
        item.expiry_date = request.POST.get('expiry_date')

        item.save()
        return redirect('dashboard')

    return render(request, 'edit_item.html', {'item': item})
