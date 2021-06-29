# Generated by Django 3.2.4 on 2021-06-25 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('telegram_id', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('telegram_username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телеграм')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=10, null=True, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('registration_time', models.DateTimeField()),
                ('language', models.CharField(blank=True, choices=[('RUS', 'rus'), ('UZB', 'uzb'), ('ENG', 'eng')], max_length=10, null=True, verbose_name='Язык')),
                ('is_admin', models.IntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]