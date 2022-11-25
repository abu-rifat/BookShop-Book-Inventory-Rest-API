# Generated by Django 4.1.3 on 2022-11-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=255, verbose_name='ISBN')),
                ('title', models.TextField(verbose_name='Title')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('published', models.CharField(max_length=255, verbose_name='Published Date')),
                ('publisher', models.CharField(max_length=255, verbose_name='Publisher')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('available', models.IntegerField(verbose_name='No of Books Available')),
            ],
        ),
    ]