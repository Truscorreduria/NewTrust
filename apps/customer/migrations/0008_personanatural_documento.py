# Generated by Django 4.2.2 on 2023-07-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_personajuridica_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='personanatural',
            name='documento',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
