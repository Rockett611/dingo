# Generated by Django 4.2.1 on 2023-05-29 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0003_result_math_result'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='math',
            options={'ordering': ['-id']},
        ),
    ]
