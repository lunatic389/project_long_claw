# Generated by Django 3.0.6 on 2020-07-03 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20200701_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]