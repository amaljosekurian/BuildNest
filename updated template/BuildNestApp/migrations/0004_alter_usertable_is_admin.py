# Generated by Django 4.2.5 on 2023-11-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuildNestApp', '0003_usertable_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
