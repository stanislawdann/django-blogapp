# Generated by Django 3.1.7 on 2021-04-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(null=True, upload_to='images', verbose_name='Obrazek'),
        ),
    ]