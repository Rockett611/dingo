# Generated by Django 4.2.1 on 2023-05-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
