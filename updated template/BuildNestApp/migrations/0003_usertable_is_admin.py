# Generated by Django 4.2.5 on 2023-11-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuildNestApp', '0002_alter_usertable_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
