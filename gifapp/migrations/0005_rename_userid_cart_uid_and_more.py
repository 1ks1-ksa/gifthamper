# Generated by Django 4.1.5 on 2023-02-20 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0004_remove_imagemodel_userid_cart_userid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='userid',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='wishlistmodel',
            old_name='userid',
            new_name='uid',
        ),
    ]
