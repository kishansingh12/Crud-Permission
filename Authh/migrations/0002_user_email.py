# Generated by Django 2.2.12 on 2022-06-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=80, null=True),
        ),
    ]
