from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from .forms import AddForm, EditForm
from django.contrib import messages

def home(request):
    data = Item.objects.filter(is_sold=False)[0:4]
    categories = Category.objects.all()
    context = {
        'data': data,
        'categories': categories
    }

    return render(request, 'base/home.html', context)

def detail(request, id):
    data = get_object_or_404(Item, id=id)
    related_data = Item.objects.filter(category=data.category, is_sold=False).exclude(id=id)[0:3]
    context = {
        'data': data,
        'related_data': related_data
    }
    
    return render(request, 'base/detail.html', context)

@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        'items' : items
    }
    return render(request, 'base/dashboard.html', context)

@login_required
def addform(request):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, "Item added successfully!!!")
            return redirect('dashboard')
    else:
        form = AddForm()
    
    context = {
        'form': form
    }
    return render(request, 'base/addform.html', context)

@login_required
def editform(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    if request.method == "POST":
        form = EditForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, "Item Updated Successfully")
            return redirect('detail', id=item.id)
    else:
        form = EditForm(instance=item)
    
    context = {
        'title': EditForm,
        'form': form
    }

    return render(request, 'base/editform.html', context)

@login_required
def delete_warning(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item
    }
    return render(request, 'base/delete_alarm.html', context)

@login_required
def delete_item(request, id):
    delete_it = get_object_or_404(Item, id=id, created_by=request.user)
    delete_it.delete()
    messages.success(request, "Item Deleted")
    return redirect('dashboard')