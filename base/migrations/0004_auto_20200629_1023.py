# Generated by Django 3.0.6 on 2020-06-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200629_0905'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientRequests',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='requeted',
            field=models.BooleanField(default=False),
        ),
    ]