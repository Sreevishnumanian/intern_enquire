# Generated by Django 4.1.5 on 2023-01-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0014_alter_message_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='comnotification',
            name='createtimestamp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='stunotification',
            name='createtimestamp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stunotification',
            name='notification',
            field=models.TextField(blank=True, null=True),
        ),
    ]
