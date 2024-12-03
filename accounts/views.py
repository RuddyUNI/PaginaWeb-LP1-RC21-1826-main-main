from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        # Lógica para el login, verificar credenciales, etc.
        # Si hay un error, por ejemplo, el usuario no existe:
        error_message = "Usuario no encontrado. Por favor, verifique sus credenciales."
        return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Verificar si el nombre de usuario ya está en uso
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
            return redirect('signup')

        # Verificar si el correo electrónico ya está en uso
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso. Por favor, utiliza otro.')
            return redirect('signup')

        # Verificar que las contraseñas coincidan
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('signup')

        # Verificar que la contraseña cumpla con los requisitos
        if len(password1) < 8 or not any(char.isdigit() for char in password1) or not any(char.isupper() for char in password1):
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres, una letra mayúscula y un número.')
            return redirect('signup')

        # Si todo está bien, crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'signup.html')
