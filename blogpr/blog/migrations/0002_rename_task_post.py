# Generated by Django 5.0.7 on 2024-08-04 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Post',
        ),
    ]