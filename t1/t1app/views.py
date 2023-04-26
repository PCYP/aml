from django.shortcuts import render
from .models import User, Data

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        access_level = request.POST['access_level']
        user = User.objects.create(username=username, password=password, access_level=access_level)
        user.save()
        return render(request, 'create_user.html', {'user': user})
    else:
        return render(request, 'create_user.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            return render(request, 'login.html', {'user': user})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def upload_data(request):
    if request.method == 'POST':
        user = request.POST['user']
        data = request.POST['data']
        tags = request.POST['tags']
        data = Data.objects.create(user=user, data=data, tags=tags)
        data.save()
        return render(request, 'upload_data.html', {'data': data})
    else:
        return render(request, 'upload_data.html')