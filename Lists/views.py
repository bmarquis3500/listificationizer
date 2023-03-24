from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, List
from .forms import ItemForm, ListForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    context = {}
    return render(request, 'Lists/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        form = ListForm()
        lists = List.objects.all()
        context = {'lists' : lists, 'form': form,}
    else:
        context = {}
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.host = request.user
            myform.save()
        else:
            form = ListForm()



    return render(request, 'Lists/home.html', context)

@login_required(login_url='login')
def list(request, pk):
    
    list = List.objects.get(id=pk)
    form = ItemForm()
    

    if request.user != list.host:
        return redirect('home')

    list_items = list.item_set.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.list = list
            myform.save()
        else:
            form = ItemForm()
    context = {'list' : list, 'list_items': list_items, 'form': form,}
    return render(request, 'Lists/list.html', context)

def deleteItem(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list', item.list.pk)

def deleteList(request, pk):
    list = get_object_or_404(List, pk = pk)
    if request.method == 'POST':
        list.delete()
        return redirect('home')
    return render(request, 'home.html')

def RegisterUser(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            #username = request.POST.get('username')
            #password = request.POST.get('password1')
            #user = User.objects.create(username=username, password = password)
            #user.save()
            user = form.save(commit= False)
            user.save()
            login(request,user)
            return redirect("home")
        
    else:
        form = RegistrationForm()
        
    context = {'form' : form}
    return render(request, 'Lists/register.html', context)