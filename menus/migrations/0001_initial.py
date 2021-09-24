# Generated by Django 2.2 on 2021-09-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('name_eng', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('img_path', models.CharField(max_length=255)),
            ],
        ),
    ]
