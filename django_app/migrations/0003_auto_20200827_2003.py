# Generated by Django 3.0.3 on 2020-08-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20200827_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='django_app/profile_pics'),
        ),
    ]
