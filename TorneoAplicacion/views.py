from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.template import loader
from .models import productos

# Create your views here.

def Productos(request):
    #return HttpResponse("<h1>Nuestra primera vista!</h1>")
    misProductos = productos.objects.all().values()
    template = loader.get_template('productos.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    return render(request, 'index.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def logros(request):
    return render(request, 'logros.html')

def politica_privacidad(request):
    return render(request, 'politica_privacidad.html')

def noticias(request):
    return render(request, 'noticias.html')

def enlaces_interes(request):
    return render(request, 'enlaces_interes.html')

def contacto(request):
    return render(request, 'contacto.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Intentar autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si el usuario existe y la contraseña es correcta, iniciar sesión
            login(request, user)
            
            # Si el usuario es un superusuario (administrador), redirigir a /admin/
            if user.is_superuser:
                return redirect('/admin')
            
            # Si no es superusuario, redirigir a la página principal
            return redirect('principal')  # Aquí deberías poner la URL de tu página principal
        else:
            # Si el usuario no existe o las credenciales son incorrectas
            messages.error(request, "Usuario o contraseña incorrectos. Si no tienes una cuenta, <a href='{% url 'signup' %}'>regístrate aquí</a>.")
            return redirect('login')  # Volver al formulario de login
    
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validaciones
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('signup')  # Volver al formulario de registro

        if len(password1) < 8:
            messages.error(request, "La contraseña debe tener al menos 8 caracteres.")
            return redirect('signup')  # Volver al formulario de registro

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Ya existe una cuenta con ese correo electrónico.")
            return redirect('signup')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Iniciar sesión automáticamente
        login(request, user)

        # Redirigir a la página de login (o a una página de inicio si lo prefieres)
        return redirect('login')

    return render(request, 'signup.html')

def torneo(request):
    return render(request, 'torneo.html')

def super_smash_bros(request):
    return render(request, 'super_smash_bros.html')

def fifa(request):
    return render(request, 'fifa.html')

def call_of_duty(request):
    return render(request, 'call_of_duty.html')


from django.shortcuts import render

def logros(request):
    # Logros de la empresa
    logros_empresa = [
        {"titulo": "Lanzamiento de la Plataforma", "descripcion": "Hemos lanzado nuestra plataforma con éxito, ofreciendo torneos en línea para gamers.", "fecha": "2024-01-10"},
        {"titulo": "1,000 Usuarios Activos", "descripcion": "Hemos alcanzado 1,000 usuarios activos registrados en nuestra plataforma.", "fecha": "2024-02-15"},
        {"titulo": "Alianzas Estratégicas", "descripcion": "Establecimos alianzas con marcas líderes en la industria de videojuegos.", "fecha": "2024-03-05"},
        {"titulo": "Nuevo Sistema de Torneos", "descripcion": "Implementamos un sistema automatizado para la gestión de torneos, mejorando la experiencia del usuario.", "fecha": "2024-04-20"},
        {"titulo": "Patrocinadores Principales", "descripcion": "Conseguimos nuestros primeros patrocinadores importantes, elevando el nivel de nuestros torneos.", "fecha": "2024-06-01"},
        {"titulo": "Evento Internacional", "descripcion": "Organizamos el primer torneo internacional con jugadores de todo el mundo.", "fecha": "2024-07-30"},
        {"titulo": "Expansión a Nuevos Mercados", "descripcion": "Comenzamos la expansión de nuestros torneos a nuevos países, alcanzando audiencia internacional.", "fecha": "2024-09-10"},
        {"titulo": "Mejoras en la Plataforma", "descripcion": "Actualizamos la interfaz de usuario de la plataforma para mejorar la navegación y la experiencia.", "fecha": "2024-10-15"},
        {"titulo": "Reconocimiento en la Industria", "descripcion": "Fuimos reconocidos como uno de los mejores sitios de torneos en línea de 2024.", "fecha": "2024-11-05"},
        {"titulo": "Comunidad Activa", "descripcion": "Nuestra comunidad creció a más de 10,000 miembros activos que participan activamente en los torneos.", "fecha": "2024-12-01"},
    ]
    
    return render(request, 'logros.html', {'logros': logros_empresa})


from django.shortcuts import render, get_object_or_404
from .models import Noticia

def noticias(request):
    noticias_list = Noticia.objects.all()  # Obtener todas las noticias
    return render(request, 'noticias.html', {'noticias': noticias_list})

def noticia_detalle(request, id):
    noticia = get_object_or_404(Noticia, id=id)  # Obtener una noticia específica
    return render(request, 'noticia_detalle.html', {'noticia': noticia})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .models import Torneo, Inscripcion
from .forms import TorneoForm, InscripcionForm
from django.contrib import messages

# Vista para mostrar torneos y permitir inscripción
def torneos_view(request):
    torneos = Torneo.objects.all()
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.usuario = request.user
            inscripcion.save()

            # Enviar correo de confirmación
            send_mail(
                'Confirmación de Inscripción',
                f'Has sido inscrito en el torneo {inscripcion.torneo.nombre}.',
                'noreply@torneosgamingsrd.com',
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, f'¡Te has inscrito en el torneo {inscripcion.torneo.nombre}!')
            return redirect('torneos')  # Redirigir a la misma página
    else:
        form = InscripcionForm()

    return render(request, 'torneos.html', {'torneos': torneos, 'form': form})

# Vista para crear torneos (solo admin)
@login_required
@user_passes_test(lambda user: user.is_superuser)
def crear_torneo_view(request):
    if request.method == 'POST':
        form = TorneoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Torneo creado exitosamente.')
            return redirect('torneos')  # Redirigir a la vista de torneos
    else:
        form = TorneoForm()
    return render(request, 'crear_torneo.html', {'form': form})

# Vista para la administración de inscripciones (solo admin)
@login_required
@user_passes_test(lambda user: user.is_superuser)
def admin_inscripciones_view(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'admin_inscripciones.html', {'inscripciones': inscripciones})


def Principal(request):
    return render(request, 'torneos.html')

from django.shortcuts import render
from .models import Torneo

def torneos_lista(request):
    torneos = Torneo.objects.all()  # Obtener todos los torneos
    return render(request, 'torneos_lista.html', {'torneos': torneos})

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from .models import Torneo, Inscripcion

def inscribirse_torneo(request, torneo_id):
    torneo = get_object_or_404(Torneo, id=torneo_id)

    # Crear la inscripción
    if request.user.is_authenticated:
        inscripcion = Inscripcion.objects.create(user=request.user, torneo=torneo)

        # Enviar correo de confirmación
        send_mail(
            'Confirmación de Inscripción al Torneo',
            f'Hola {request.user.username},\n\nTe has inscrito con éxito al torneo: {torneo.nombre}.',
            'no-reply@torneosgamingsrd.com',
            [request.user.email],
            fail_silently=False,
        )

        # Redirigir a la página de torneos o una página de confirmación
        return redirect('torneos_lista')

    return redirect('login')  # Si no está logueado, redirigir al login