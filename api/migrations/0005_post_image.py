# Generated by Django 3.2.2 on 2021-05-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210526_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/% Y/% m/% d/'),
        ),
    ]