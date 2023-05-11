from django.db import models

class alumnos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.IntegerField(verbose_name="nombre")
    apellido=models.IntegerField(verbose_name="apellido")
    tipoidentificacion=models.CharField(max_length=100, verbose_name="tipoidentificacion")
    numeroid=models.IntegerField(verbose_name="numeroid")
    fechanacimiento=models.DateField(null="True")
    semestre=models.IntegerField(verbose_name="semestre")
    fecharegistro=models.DateField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'alumnos'

class alumnoss(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30, null=False)
    apellido=models.CharField(max_length=30, null=False)
    tipoidentificacion=models.CharField(max_length=30, null=False)
    numeroid=models.CharField(max_length=30, null=False)
    fechanacimiento=models.DateField(null="True")
    semestre=models.IntegerField(null=False)
    fecharegistro=models.DateField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'alumnoss'

class cursos(models.Model):
    id=models.AutoField(primary_key=True)
    nombrecurso=models.CharField(max_length=30, null=False)
    codigocurso=models.CharField(max_length=30, null=False)
    creditos=models.IntegerField(null=False)
    fecharegistro=models.DateField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'cursos'

class fichaalumnos(models.Model):
    id=models.AutoField(primary_key=True)
    nombrealumno=models.CharField(max_length=30, null=False)
    cursomatriculado=models.CharField(max_length=30, null=False)
    correoalumno=models.CharField(max_length=30, null=False)
    fecharegistro=models.DateField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'fichaalumnos'


class ficha(models.Model):
    id=models.AutoField(primary_key=True)
    nombrealumno=models.CharField(max_length=60, null=False)
    cursomatriculado=models.CharField(max_length=60, null=False)
    correoalumno=models.CharField(max_length=30, null=False)
    fecharegistro=models.DateField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'ficha'

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(alumnoss, on_delete=models.CASCADE)
    curso = models.ForeignKey(cursos, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'registros'

class centros(models.Model):
    id=models.AutoField(primary_key=True)
    nombrecentro=models.CharField(max_length=40, null=False)
    extension=models.CharField(max_length=30, null=False)
    direccion=models.CharField(max_length=30, null=False)
    fecharegistro=models.DateField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'centros'