# Generated by Django 3.2.7 on 2021-10-05 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='BlogPost',
        ),
    ]