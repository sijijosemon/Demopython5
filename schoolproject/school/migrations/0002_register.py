# Generated by Django 4.1.7 on 2023-06-08 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('purpose', models.CharField(max_length=250)),
                ('materials_provide', models.CharField(max_length=250)),
            ],
        ),
    ]
