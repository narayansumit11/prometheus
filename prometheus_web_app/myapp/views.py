from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import CustomUserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user.set_password(password)
            new_user.save()
            authenticate(username=username, password=password)
            login(request, new_user)
            request.session['is_connected'] = True
            return redirect('/home')

        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')  # profile
        else:
            msg = 'Invalid User Name or Password'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def profile(request):
    return render(request, 'home.html')


def signout(request):
    logout(request)
    return redirect('/home')