# Generated by Django 5.0.6 on 2024-06-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
