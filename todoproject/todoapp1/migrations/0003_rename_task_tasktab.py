# Generated by Django 4.0.3 on 2022-04-04 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp1', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='task',
            new_name='tasktab',
        ),
    ]