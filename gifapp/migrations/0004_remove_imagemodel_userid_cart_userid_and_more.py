# Generated by Django 4.1.5 on 2023-02-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0003_imagemodel_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='userid',
        ),
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]