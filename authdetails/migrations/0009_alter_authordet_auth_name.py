# Generated by Django 4.0.3 on 2022-11-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authdetails', '0008_alter_authordet_auth_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordet',
            name='auth_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
