# Generated by Django 4.1.5 on 2023-02-21 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0006_shopnotimodel_usernotimodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopnotimodel',
            name='date',
        ),
        migrations.RemoveField(
            model_name='usernotimodel',
            name='date',
        ),
        migrations.AddField(
            model_name='shopnotimodel',
            name='shopdate',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usernotimodel',
            name='userdate',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
