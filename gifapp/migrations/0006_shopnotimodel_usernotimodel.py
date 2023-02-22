# Generated by Django 4.1.5 on 2023-02-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0005_rename_userid_cart_uid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopnotimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='usernotimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
