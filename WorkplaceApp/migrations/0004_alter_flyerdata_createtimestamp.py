# Generated by Django 4.1.5 on 2023-01-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0003_studentdatatable_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flyerdata',
            name='createtimestamp',
            field=models.CharField(max_length=1000),
        ),
    ]