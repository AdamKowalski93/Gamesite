# Generated by Django 2.0.7 on 2018-07-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='ImageGame',
            field=models.ImageField(upload_to='images'),
        ),
    ]
