# Generated by Django 4.2.4 on 2023-08-02 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pontosturisticos', '0004_pontosturisticos_enderecos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontosturisticos',
            old_name='enderecos',
            new_name='endereco',
        ),
    ]
