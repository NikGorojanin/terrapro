# Generated by Django 3.2.4 on 2021-06-25 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('en_name', models.CharField(max_length=100)),
                ('ru_name', models.CharField(blank=True, max_length=100, null=True)),
                ('uz_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cites',
            },
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('telegram_id', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('telegram_username', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('tg_voice_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'feedback_messages',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('tg_image_id', models.CharField(blank=True, max_length=200, null=True)),
                ('tg_video_id', models.CharField(blank=True, max_length=200, null=True)),
                ('tg_document_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Branche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='branches', to='account.user')),
            ],
            options={
                'db_table': 'branches',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('barcode', models.IntegerField()),
                ('phone_number', models.CharField(max_length=100)),
                ('total_balance', models.FloatField()),
                ('total_spent_monthly', models.FloatField()),
                ('total_spent_yearly', models.FloatField()),
                ('total_spent', models.FloatField()),
                ('birthday', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='accounts', to='account.user')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]