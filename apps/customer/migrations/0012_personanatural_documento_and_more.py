# Generated by Django 4.2.2 on 2023-08-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_personanatural_documento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personanatural',
            name='documento',
            field=models.FileField(null=True, upload_to='document/persona_natural'),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='documento',
            field=models.FileField(null=True, upload_to='document/persona_juridica'),
        ),
    ]