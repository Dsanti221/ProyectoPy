# Generated by Django 3.2.8 on 2023-05-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_registro_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='centros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrecentro', models.CharField(max_length=40)),
                ('extension', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('fecharegistro', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'centros',
            },
        ),
    ]
