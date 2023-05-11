from datetime import date
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import alumnoss,ficha,Registro, cursos, alumnos #SI quieroagregar mas modelos aqui con coma
from django.utils.timezone import now
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render
import datetime
from .models import cursos, cursos , centros 

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.shortcuts import render


from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Registro
from .forms import RegistroForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse




# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request,'indexx.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Verifica las contraseñas no son las mismas!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("El usuario o la contraseña son incorrectos!!!")

    return render (request,'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def CrearAlumno(request):
   if request.method=='POST':
       #se agregan los datos
       if request.POST.get('nombre') and request.POST.get('apellidos') and request.POST.get('tipoid') and request.POST.get('numero') and request.POST.get('fecha') and request.POST.get('semestre'):
           insertalu= alumnoss()
           insertalu.nombre=request.POST.get('nombre')
           insertalu.apellido=request.POST.get('apellidos')
           insertalu.tipoidentificacion=request.POST.get('tipoid')
           insertalu.numeroid=request.POST.get('numero')
           insertalu.fechanacimiento=request.POST.get('fecha')
           insertalu.semestre=request.POST.get('semestre')
           insertalu.save()
           return redirect('listaralumno')
   else:
       #devuelve el formulario
       return render (request,'crudalumnos/crear.html')
   


@login_required(login_url='login')
def EditarAlumno(request,idAlumnoss):
    try:
        if request.method=='POST':
        #se agregan los datos
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellidos') and request.POST.get('tipoid') and request.POST.get('numero') and request.POST.get('fecha') and request.POST.get('semestre'):
                alu_id_old= request.POST.get('id')
                alu_old=alumnoss()
                alu_old=alumnoss.objects.get(id=alu_id_old)
                
                
                insertalu= alumnoss()
                insertalu.id=request.POST.get('id')
                insertalu.nombre=request.POST.get('nombre')
                insertalu.apellido=request.POST.get('apellidos')
                insertalu.tipoidentificacion=request.POST.get('tipoid')
                insertalu.numeroid=request.POST.get('numero')
                insertalu.fechanacimiento=request.POST.get('fecha')
                insertalu.semestre=request.POST.get('semestre')
                insertalu.fecharegistro=alu_old.fecharegistro
                
                insertalu.save()
                return redirect('listaralumno')
        else:   
            alu = alumnoss.objects.all()
            insertalu = alumnoss.objects.get(id=idAlumnoss)
            datos = {'alumnoss': alu, 'alumnos': insertalu}
            return render (request,'crudalumnos/modificar.html',datos)
    except alumnoss.DoesNotExist:
        alu = alumnoss.objects.all()
        insertalu = None
        datos = {'alumnoss': alu, 'alumnos': insertalu}
        return render (request,'crudalumnos/modificar.html',datos)
    




@login_required(login_url='login')
def ListarAlumno(request):
    if request.method=='POST':
        palabra = request.POST.get('keyword')
        lista = alumnoss.objects.all()

        if palabra is not None:

           
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) | 
                Q(nombre__icontains=palabra) | 
                Q(apellido__icontains=palabra) |
                Q(tipoidentificacion__icontains=palabra) |
                Q(numeroid__icontains=palabra) |
                Q(fechanacimiento__icontains=palabra) |
                Q(semestre__icontains=palabra) 
            )
            datos ={'alumnoss': resultado_busqueda }
            return render (request,'crudalumnos/listar.html', datos)
        else:
            datos = {'alumnoss': lista}
            return render (request,'crudalumnos/listar.html', datos)

    else:    
        alu = alumnoss.objects.order_by('id')[:20]
        datos = {'alumnoss': alu}
        return render (request,'crudalumnos/listar.html', datos)

@login_required(login_url='login')
def EliminarAlumno(request,idAlumnoss):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = alumnoss.objects.get(id=id_a_borrar)
                tupla.delete()
                return redirect('listaralumno')
        else:    
            alu = alumnoss.objects.all()
            insertalu = alumnoss.objects.get(id=idAlumnoss)
            datos = {'alumnoss': alu, 'alumnos': insertalu} 
            return render (request,'crudalumnos/eliminar.html',datos)
          
    except alumnoss.DoesNotExist:
        alu = alumnoss.objects.all()
        insertalu = None
        datos = {'alumnoss': alu, 'alumnos': insertalu}
        return render (request,'crudalumnos/eliminar.html',datos)
    

@login_required(login_url='login')
def CrearCurso(request):
   if request.method=='POST':
       #se agregan los datos
       if request.POST.get('nombre') and request.POST.get('codigo') and request.POST.get('creditoid'):
           insertalu= cursos()
           insertalu.nombrecurso=request.POST.get('nombre')
           insertalu.codigocurso=request.POST.get('codigo')
           insertalu.creditos=request.POST.get('creditoid')
           insertalu.save()
           return redirect('listarcurso')
   else:
       #devuelve el formulario
       return render (request,'crudcursos/crear.html')
   


@login_required(login_url='login')
def EditarCurso(request,idCursos):
    try:
        if request.method=='POST':
        #se agregan los datos
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('codigo') and request.POST.get('credito'):
                alu_id_old= request.POST.get('id')
                alu_old=cursos()
                alu_old=cursos.objects.get(id=alu_id_old)
                
                
                insertalu= cursos()
                insertalu.id=request.POST.get('id')
                insertalu.nombrecurso=request.POST.get('nombre')
                insertalu.codigocurso=request.POST.get('codigo')
                insertalu.creditos=request.POST.get('credito')
                insertalu.fecharegistro=alu_old.fecharegistro
                
                insertalu.save()
                return redirect('listarcurso')
        else:   
            alu = cursos.objects.all()
            insertalu = cursos.objects.get(id=idCursos)
            datos = {'cursos': alu, 'cursoss': insertalu}
            return render (request,'crudcursos/modificar.html',datos)
    except cursos.DoesNotExist:
        alu = cursos.objects.all()
        insertalu = None
        datos = {'cursos': alu, 'cursoss': insertalu}
        return render (request,'crudcursos/modificar.html',datos)
    




@login_required(login_url='login')
def ListarCurso(request):
    alu = cursos.objects.all()
    datos = {'cursos': alu}
    return render (request,'crudcursos/listar.html', datos)
 
       
@login_required(login_url='login')
def EliminarCurso(request,idCursos):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = cursos.objects.get(id=id_a_borrar)
                tupla.delete()
                return redirect('listarcurso')
        else:    
            alu = cursos.objects.all()
            insertalu = cursos.objects.get(id=idCursos)
            datos = {'cursos': alu, 'cursoss': insertalu} 
            return render (request,'crudcursos/eliminar.html',datos)
          
    except cursos.DoesNotExist:
        alu = cursos.objects.all()
        insertalu = None
        datos = {'cursos': alu, 'cursoss': insertalu}
        return render (request,'crudcursos/eliminar.html',datos)



@method_decorator(login_required, name='dispatch')
class RegistroView(CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'crudfichaalumno/crear.html'
    success_url = reverse_lazy('registro_exitoso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alumnos'] = alumnoss.objects.all()
        context['cursos'] = cursos.objects.all()
        return context

    def form_valid(self, form):
        form.instance.alumno = alumnoss.objects.get(id=self.request.POST.get('alumno'))
        form.instance.curso = cursos.objects.get(id=self.request.POST.get('curso'))
        return super().form_valid(form)

@login_required(login_url='login')
def registro_exitoso_view(request):
    return render(request, 'registro_exitoso.html')

@login_required(login_url='login')
def ListarFicha(request):
    #alu = Registro.objects.all()
    alu = Registro.objects.all().order_by('alumno')
    datos = {'cursos': alu}
    return render (request,'crudfichaalumno/listar.html', datos)

@login_required(login_url='login')
def EliminarFicha(request,idCursos):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Registro.objects.get(id=id_a_borrar)
                tupla.delete()
                return redirect('listarfichaalumno')
        else:    
            alu = Registro.objects.all()
            insertalu = Registro.objects.get(id=idCursos)
            datos = {'cursos': alu, 'cursoss': insertalu} 
            return render (request,'crudfichaalumno/eliminar.html',datos)
          
    except Registro.DoesNotExist:
        alu = Registro.objects.all()
        insertalu = None
        datos = {'cursos': alu, 'cursoss': insertalu}
        return render (request,'crudfichaalumno/eliminar.html',datos)
    
@login_required(login_url='login')
def ListarFichaCursos(request):
    return render (request,'crudfichacursos/listar.html')    



@login_required(login_url='login')
def CrearCentro(request):
   if request.method=='POST':
       #se agregan los datos
       if request.POST.get('nombre') and request.POST.get('ext') and request.POST.get('dir'):
           insertalu= centros()
           insertalu.nombrecentro=request.POST.get('nombre')
           insertalu.extension=request.POST.get('ext')
           insertalu.direccion=request.POST.get('dir')
           insertalu.save()
           return redirect('listarcentro')
   else:
       #devuelve el formulario
       return render (request,'crudcentro/crear.html')

@login_required(login_url='login')
def ListarCentro(request):
    alu = centros.objects.all()
    datos = {'centros': alu}
    return render (request,'crudcentro/listar.html', datos)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            return auth_views.PasswordResetView.as_view(
                template_name='registration/password_reset_form.html',
                email_template_name='registration/password_reset_email.html',
                subject_template_name='registration/password_reset_subject.txt',
            )(request, from_email=password_reset_form.cleaned_data['email'])
    else:
        password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form": password_reset_form})


def password_reset_done(request):
    return auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html')(request)


def password_reset_confirm(request, uidb64, token):
    return auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/password_reset_complete/'
    )(request, uidb64=uidb64, token=token)


def password_reset_complete(request):
    return auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html')(request)






