# Generated by Django 3.2.4 on 2021-06-28 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_id_1c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_1c',
        ),
    ]
