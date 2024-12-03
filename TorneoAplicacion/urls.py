from django.urls import path
from . import views

urlpatterns = [
    path('Productos/', views.Productos, name='Productos'),
    path('', views.index, name='index'),
    path('torneo/', views.torneo, name='torneo'),
    path('torneo/super_smash_bros', views.super_smash_bros, name='super_smash_bros'),
    path('torneo/fifa', views.fifa, name='fifa'),
    path('torneo/call_of_duty', views.call_of_duty, name='call_of_duty'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('logros/', views.logros, name='logros'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('enlaces-interes/', views.enlaces_interes, name='enlaces_interes'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logros/', views.logros, name='logros'),
     path('noticias/', views.noticias, name='noticias'),  # Lista de noticias
    path('noticia/<int:id>/', views.noticia_detalle, name='noticia_detalle'),
    path('torneos/', views.torneos_view, name='torneos'),
    path('crear_torneo/', views.crear_torneo_view, name='crear_torneo'),
    path('admin/inscripciones/', views.admin_inscripciones_view, name='admin_inscripciones'),
    path('accounts/profile/', views.Principal, name="Principal"),
    path('torneos/', views.torneos_lista, name='torneos_lista'),
    path('inscribirse/<int:torneo_id>/', views.inscribirse_torneo, name='inscribirse_torneo'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)