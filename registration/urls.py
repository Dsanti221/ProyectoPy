"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('admin', admin.site.urls),
    path('signup',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('index',views.HomePage,name='home'),
    path('logout',views.LogoutPage,name='logout'),
    path('crearalumno',views.CrearAlumno,name='crearalumno'),
    path('modificaralumno/<int:idAlumnoss>',views.EditarAlumno,name='modificaralumno'),
    path('listaralumno',views.ListarAlumno,name='listaralumno'),
    path('eliminaralumno/<int:idAlumnoss>',views.EliminarAlumno,name='eliminaralumno'),

    path('crearcurso',views.CrearCurso,name='creacurso'),
    path('modificarcurso/<int:idCursos>',views.EditarCurso,name='modificarcurso'),
    path('listarcurso',views.ListarCurso,name='listarcurso'),
    path('eliminarcurso/<int:idCursos>',views.EliminarCurso,name='eliminarcurso'),

    path('crearcentro',views.CrearCentro,name='creacentro'),
    path('listarcentro',views.ListarCentro,name='listarcentro'),
      
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('password_reset/done/', views.password_reset_done, name="password_reset_done"),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name="password_reset_confirm"),
    path('password_reset_complete/', views.password_reset_complete, name="password_reset_complete"),



    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('registro-exitoso/', views.registro_exitoso_view, name='registro_exitoso'),
    path('listarfichaalumno',views.ListarFicha,name='listarfichaalumno'),
    path('eliminarfichaalumno/<int:idCursos>',views.EliminarFicha,name='eliminarfichaalumno'),
    
    path('listarfichacurso',views.ListarFichaCursos,name='listarfichacurso'),


]