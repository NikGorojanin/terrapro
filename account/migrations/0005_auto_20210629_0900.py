# Generated by Django 3.2.4 on 2021-06-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_id_1c'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_1c',
            field=models.CharField(db_index=True, default=1, max_length=100, unique=True, verbose_name='1C ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
