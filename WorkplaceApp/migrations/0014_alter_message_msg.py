# Generated by Django 4.1.5 on 2023-01-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0013_stunotification_message_comnotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg',
            field=models.TextField(blank=True, null=True),
        ),
    ]