from django.shortcuts import render,redirect,get_object_or_404
from .forms import CafePost,CommentForm
from django.db import transaction
from .models import Cafe
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Profile

# Create your views here.
def home(request): 
    cafes = Cafe.objects
    ceo = True if (Profile.ceo == True) else False
    print(ceo)
    return render(request, 'home.html', {'cafes':cafes, 'ceo':ceo})


# def newcafe(request):
#     return render(request, 'newcafe.html')

def newcafe(request):
    if request.method =='POST':
        form = CafePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            return redirect('home')
            
    else:
        form = CafePost()
        # image_form = ImagePost(instance=request.cafe.image)
    return render(request,'newcafe.html',{'form':form})


def detail(request, cafe_id):
    cafes = get_object_or_404(Cafe, pk=cafe_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user
            comment.post = cafes
            comment.save()
            return redirect('detail', pk=cafe_id)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'cafes':cafes,'form': form})   

def search(request):
    qs = Cafe.objects.all()
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(name__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    return render(request, 'home.html', {'cafe_list' : qs,'q' : q,})