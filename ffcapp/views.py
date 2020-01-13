from django.shortcuts import render,redirect
from .forms import CafePost,ImagePost
from django.db import transaction
from .models import Cafe

# Create your views here.
def home(request): 
    cafes = Cafe.objects
    return render(request, 'home.html', {'cafes':cafes})

def connect(request):
    return render(request, 'connect.html')

# def newcafe(request):
#     return render(request, 'newcafe.html')

def newcafe(request):
    if request.method =='POST':
        form = CafePost(request.POST)
        image_form =  ImagePost(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            # form.save()
            cafepost = form.save(commit=False)
            cafepost.user = request.user
            cafepost.save()
            image_form.save()            
            return redirect('home')
    else:
        form = CafePost()
        upimage = ImagePost()
    return render(request,'newcafe.html',{'form':form,'upimage':upimage,})