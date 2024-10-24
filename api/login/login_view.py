from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def login_view(request):
    template_name ="auth-login.html"

    if  request.user.is_active and request.user.is_active:
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
                login(request, user)
                return redirect('Home')
        else:
            
                messages.error(request, 'inavalid login credentials or user is not active')
    return render(request,template_name)

#view for register
def register_view(request):
    template_name = "auth-register.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # Check if passwords match
        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, template_name)

        # Create new user
        user = User(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()

        messages.success(request, 'Cuenta creada exitosamente')
        return redirect('login')

    # Render the registration page if not POST
    return render(request, template_name)

#view forgot
def forgot_view(request):
    template_name ="auth-forgot-password.html"
    return render(request,template_name)

#logout
def logout_view(request):
    logout(request)
    return redirect('login')




