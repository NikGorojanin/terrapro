# Generated by Django 3.2.4 on 2021-06-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='id_1c',
            field=models.CharField(db_index=True, default=1, max_length=100, unique=True, verbose_name='1C ID'),
            preserve_default=False,
        ),
    ]
