# Generated by Django 4.0.3 on 2022-11-21 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authdetails', '0004_alter_authordet_auth_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='authorDet',
            new_name='authorDetails',
        ),
        migrations.RenameModel(
            old_name='bookDet',
            new_name='bookDetails',
        ),
        migrations.RenameField(
            model_name='authordetails',
            old_name='auth_age',
            new_name='author_age',
        ),
        migrations.RenameField(
            model_name='authordetails',
            old_name='auth_country',
            new_name='author_country',
        ),
        migrations.RenameField(
            model_name='authordetails',
            old_name='auth_gender',
            new_name='author_gender',
        ),
        migrations.RenameField(
            model_name='authordetails',
            old_name='auth_name',
            new_name='author_name',
        ),
    ]
