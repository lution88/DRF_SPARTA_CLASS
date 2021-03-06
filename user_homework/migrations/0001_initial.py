# Generated by Django 4.0.5 on 2022-06-17 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='사용자계정')),
                ('email', models.EmailField(max_length=100, verbose_name='이메일')),
                ('password', models.CharField(max_length=200, verbose_name='패스워드')),
                ('fullname', models.CharField(max_length=20, verbose_name='이름')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('dt_updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
                ('introduction', models.TextField(verbose_name='소개')),
                ('birthday', models.DateField(verbose_name='생일')),
                ('age', models.IntegerField(verbose_name='나이')),
            ],
        ),
    ]
