# Generated by Django 3.1.5 on 2021-01-13 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_product',
            old_name='cart_id',
            new_name='cart_present',
        ),
    ]
