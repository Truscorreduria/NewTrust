# Generated by Django 4.2.2 on 2023-07-20 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0003_rename_departamento_subramo_ramo_and_more'),
        ('customer', '0005_alter_personajuridica_representante_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
