# Generated by Django 3.1 on 2021-04-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210404_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
