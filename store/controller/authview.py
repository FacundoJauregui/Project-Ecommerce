from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from store.forms import LoginForm, RegisterUserForm

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Successfully! Login to Continue')
            return redirect('Login')
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, "store/auth/register.html", context)

def loginRequest(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            form = LoginForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return redirect('/')
            else:
                form = LoginForm()
                messages.error(request, 'Invalid Username or Password')
                return redirect('Login')
        else:
            form = LoginForm()
        context = {'form': form}
            
        return render(request,"store/auth/login.html", context )
