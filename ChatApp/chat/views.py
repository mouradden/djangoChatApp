from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Chat
@login_required
def index(request):
    receiver_name = request.GET.get('user', None)
    data = None
    if receiver_name:
        if User.objects.filter(username=receiver_name).exists() and Chat.objects.filter(sender=request.user,receiver=User.objects.get(username=receiver_name)).exists():
            receiver_ = User.objects.get(username=receiver_name)
            data = Chat.objects.get(sender=request.user,receiver=receiver_).content
    receivers = User.objects.exclude(pk=request.user.id)
    return render(request,'index.html',{'my':data,'content': data,'receivers':receivers})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})