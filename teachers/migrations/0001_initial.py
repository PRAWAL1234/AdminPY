# Generated by Django 4.1.7 on 2024-03-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.IntegerField()),
            ],
        ),
    ]
