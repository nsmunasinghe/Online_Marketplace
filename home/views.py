from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm

def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)[0:6]

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })