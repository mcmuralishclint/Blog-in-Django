# Generated by Django 2.2.3 on 2019-07-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
