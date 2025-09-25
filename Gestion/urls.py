"""
URL configuration for Gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Vistas principales
from Cursos import views
# Vistas de la solicitud
from solicitud import views as views_solicitud
# Vistas de las consultas (La mas grande)
from consultas import views as views_consultas
# vista de las consultas del aspirante
from aspirantes import views as views_aspirantes

from programas import views as views_programas
# Importar la configuarción para usar la media y los statics
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Paginas princiales Login - Pagina inicio (Todos los roles)
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('pagina_principal/', views.login_view, name="login"),
    # Paginas de creación (Admin - Instru)
    path('crearficha/', views_solicitud.crear_solicitud, name="Crearsolicitud"),
    path('formulario_solicitud_regular/', views_solicitud.solicitud_regular, name="crearregular"),
    path('formulario_solicitud_campesina/', views_solicitud.solicitud_campesina, name="crearcampesina"),
    # Realizar las consultas dependiendo el rol que este en el sistema
    path('Consultas_instructor/', views_consultas.consultas_instructor, name="consultas_instructor"),
    # Ver la ficha de caracterización como admin e instructor
    path('ficha_caracterizacion/<int:solicitud_id>/', views_consultas.ficha_caracterizacion, name="ficha_caracterizacion"),
    # Descargar  ficha de caracterización en PDF
    path('ficha_caracterizacion/<int:solicitud_id>/pdf/', views_consultas.ficha_caracterizacion_pdf, name="ficha_caracterizacion_pdf"),
    # Formulario para la inscripción de los aspirantes
    path('preinscripcion/<int:idsolicitud>/', views_aspirantes.formulario_aspirantes, name="formularioaspirantes"),
    # Realización del registro de preinscripción
    path('preinscripcion/', views_aspirantes.registro_aspirante, name="Registroaspirantes"),
    # Descargar PDF combinado de los aspirantes
    path('pdf/<int:id>/<int:idrol>', views_consultas.descargar_pdf, name='descargar_pdf'),
    # Descargar excel
    path('descargar_excel/<int:id>/<int:idrol>', views_consultas.descargar_excel, name="descargar_excel"),
    # Descargar carta de solicitud
    path('descargar_carta/<int:id>/<int:idrol>', views_consultas.descargar_carta, name="descargar_carta"),
    # Comentarios enviados por el funcionario
    path('revision_funcionario/<int:id>/', views_consultas.revision_fichas, name="ficha_funcionario"),
    # Descargar excel subido por el funcionario
    path('descargar_formato_sofia_plus/<int:id>', views_consultas.descargar_excel_ficha, name='sofia_plus_descarga'),
    # Enviar esatdo y observación del coordinador
    path('revision_coordinador/<int:id_solicitud>/', views_consultas.revision_coordinador, name='revision_coordinador'),
    # Ver excel 
    path('ver_formato/<int:id_solicitud>/', views_consultas.ver_formato_inscripcion, name='ver_formato'),
    # Ver PDF aspirantes
    path('ver_pdf_aspirantes/<int:id_solicitud>/', views_consultas.ver_pdf_aspirantes, name="ver_pdf_aspirantes"),
    # Ver carta
    path('ver_pdf_carta/<int:id_solicitud>/', views_consultas.ver_pdf_carta, name='ver_pdf_carta'),
    # Cerrar sesión    
    path('cerrar_sesion/', views.cerrar_sesion, name='salir'),
    # Buscar programa
    path('buscar_programa/', views_programas.buscar_programas, name='buscar_programa'),
    # Editar programa 
    path('editar_programa', views_programas.editar_programa, name="actualizar_programa"),
    #Borrar programa
    path("borrar/<str:codigo>/", views_programas.borrar_programa, name="borrar_programa"),
]
# Poder almacenar archivos en la carpeta media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
