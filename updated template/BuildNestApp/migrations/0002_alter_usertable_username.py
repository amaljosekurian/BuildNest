# Generated by Django 4.2.5 on 2023-11-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuildNestApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
