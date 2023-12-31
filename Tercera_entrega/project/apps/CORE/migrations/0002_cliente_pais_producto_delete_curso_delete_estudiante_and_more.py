# Generated by Django 4.2.3 on 2023-07-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('Pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tamaño', models.CharField(max_length=100)),
                ('caracteristica', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
