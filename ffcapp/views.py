from django.shortcuts import render,redirect
from .forms import CafePost

# Create your views here.
def home(request):
    return render(request, 'home.html')

def connect(request):
    return render(request, 'connect.html')

# def newcafe(request):
#     return render(request, 'newcafe.html')

def newcafe(request):
    if request.method =='POST':
        cafe = CafePost(request.POST)
        if cafe.is_valid():
            cafe.save()
            return redirect('home')
    else:
        cafe = CafePost()
    return render(request,'newcafe.html',{'cafe':cafe})