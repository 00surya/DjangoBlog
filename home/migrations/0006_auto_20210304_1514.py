# Generated by Django 3.1.7 on 2021-03-04 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='autabout',
            new_name='Aautabout',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='email',
            new_name='Aemail',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='instalnk',
            new_name='Ainstalnk',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='Aname',
        ),
    ]
