# Generated by Django 5.0.2 on 2024-03-03 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_alter_simplecase_case'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
