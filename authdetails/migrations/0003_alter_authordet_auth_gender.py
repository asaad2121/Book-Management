# Generated by Django 4.0.3 on 2022-11-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authdetails', '0002_alter_authordet_auth_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordet',
            name='auth_gender',
            field=models.IntegerField(choices=[('M', 'male'), ('F', 'female'), ('O', 'not specified')]),
        ),
    ]
