# Generated by Django 5.1.2 on 2024-10-21 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]
