# Generated by Django 4.2.2 on 2023-07-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_delete_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='personajuridica',
            name='documento',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
