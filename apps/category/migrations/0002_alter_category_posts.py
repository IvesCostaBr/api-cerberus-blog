# Generated by Django 3.2.5 on 2021-07-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, to='post.Post'),
        ),
    ]