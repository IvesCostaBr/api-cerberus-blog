# Generated by Django 3.2.5 on 2021-07-10 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
    ]
