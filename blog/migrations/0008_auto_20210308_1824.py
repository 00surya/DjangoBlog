# Generated by Django 3.1.7 on 2021-03-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210308_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=20000),
        ),
    ]