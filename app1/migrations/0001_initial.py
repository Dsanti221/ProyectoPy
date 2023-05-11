# Generated by Django 3.2.8 on 2023-04-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumnos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.IntegerField(verbose_name='nombre')),
                ('apellido', models.IntegerField(verbose_name='apellido')),
                ('tipoidentificacion', models.CharField(max_length=100, verbose_name='tipoidentificacion')),
                ('numeroid', models.IntegerField(verbose_name='numeroid')),
                ('fechanacimiento', models.DateField(null='True')),
                ('semestre', models.IntegerField(verbose_name='semestre')),
                ('fecharegistro', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'alumnos',
            },
        ),
    ]