# Generated by Django 2.2.10 on 2020-05-08 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Orden')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('url_code', models.URLField(max_length=255, verbose_name='URL código')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Ultima edición')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'ordering': ['order', '-id'],
            },
        ),
    ]
