from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Simu, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    simus = Simu.objects.all()
    context = {'simus' : simus}
    return render(request, 'simu/index.html', context)

def detail(request, simu_id):
    simu = Simu.objects.get(id=simu_id)

    context = {'simu': simu}

    return render(request, 'simu/detail.html', context)

@login_required
def new(request):
    return render(request, "simu/new.html")

@login_required
def create(request):
    user = request.user
    body = request.POST['body']
    simu = Simu(user=user, body=body, created_at=timezone.now())
    simu.save()

    return redirect('simus:detail', simu_id=simu.id)

@login_required
def edit(request, simu_id):
    try:
        simu = Simu.objects.get(id=simu_id, user=request.user)
    except Simu.DoesNotExist:
        return redirect('simus:index')
    context = {'simu' : simu}
    return render(request, 'simu/edit.html', context)

@login_required
def update(request, simu_id):
    try:
        simu = Simu.objects.get(id=simu_id, user=request.user)
    except Simu.DoesNotExist:
        return redirect('simus:index')

    simu.body = request.POST['body']
    simu.save()
    return redirect('simus:detail', simu_id=simu.id)

@login_required
def delete(request, simu_id):
    try:
        simu = Simu.objects.get(id=simu_id, user=request.user)
    except Simu.DoesNotExist:
        return redirect('simus:index')

    simu.delete()
    return redirect('simus:index')

def search_result(request):
    simu_object = Simu.objects.all() # 검색할 객체를 가져오는 과정입니다. Post모델 안의 모든 객체를 post_object 변수 안에 담아줍니다.
    query = request.GET.get('query','') # query에 담긴 값을 '', 즉 빈 문자열 안에 채워넣어 오도록 하겠습니다. 
    if query: # 쿼리값이 존재한다면
        simu_object = simu_object.filter(body__contains=query) 
        # 쿼리값과 일치하는, 즉 쿼리값으로 끝나는 타이틀을 가진 객체를 필터링하여 post_object에 담아줍니다.
        return render(request,'simu/search_result.html',{'result':simu_object})
        # Simu.objects.all() -> simu_object -> 'result'

@login_required
def like(request, simu_id):

    if request.method == 'POST':
        try:
            simu = Simu.objects.get(id=simu_id)

            if request.user in simu.liked_users.all():
                simu.liked_users.remove(request.user)
            else:
                simu.liked_users.add(request.user)
            
            return redirect('simus:detail', simu_id=simu_id)
        
        except Simu.DoesNotExist:
            pass
    
    return redirect('simus:index')

    from .models import Blog, Comment