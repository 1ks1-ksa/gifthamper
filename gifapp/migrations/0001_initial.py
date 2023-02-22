# Generated by Django 4.1.5 on 2023-02-16 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='billmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('add', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='buymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronm', models.CharField(max_length=30)),
                ('propri', models.IntegerField()),
                ('prode', models.CharField(max_length=30)),
                ('prfl', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=30)),
                ('proprice', models.IntegerField()),
                ('prodes', models.CharField(max_length=30)),
                ('prfile', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='imagemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=30)),
                ('proprice', models.IntegerField()),
                ('prodes', models.CharField(max_length=30)),
                ('prfile', models.ImageField(upload_to='gifapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='onlinepaymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=40)),
                ('cardnumber', models.CharField(max_length=40)),
                ('cardexpiry', models.CharField(max_length=40)),
                ('securitycode', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='shopregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('shopid', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='wishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=30)),
                ('proprice', models.IntegerField()),
                ('prodes', models.CharField(max_length=30)),
                ('prfile', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
