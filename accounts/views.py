from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
   

def ceosignup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['ceopassword1'] == request.POST['ceopassword2']:
            try:
                ceo = Ceo.objects.get(ceoid=request.POST['ceoid'])
                return render(request, 'ceosignup.html', {'error': 'Username has already been taken'})
            except Ceo.DoesNotExist:
                ceo = Ceo.objects.create_ceo(
                    request.POST['ceoid'], ceopassword=request.POST['ceopassword1'])
                auth.login(request, ceo)
                return redirect('home')
        else:
            return render(request, 'ceosignup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'ceosignup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')

# def ceosignup(request):
#     if request.method =='POST':
#         form = ceosignup(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.pub_date=timezone.now()
#             post.save()
#             return redirect('home')
#     else:
#         form = BlogPost()
#         return render(request,'new.html',{'form':form})