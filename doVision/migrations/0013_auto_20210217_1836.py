# Generated by Django 3.1.5 on 2021-02-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doVision', '0012_auto_20210217_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(default=None),
        ),
    ]
