# Generated by Django 2.2.10 on 2020-05-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
        migrations.AddField(
            model_name='link',
            name='icon_class_css',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Icono de clase css'),
        ),
    ]