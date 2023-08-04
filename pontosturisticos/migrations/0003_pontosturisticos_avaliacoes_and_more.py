# Generated by Django 4.2.4 on 2023-08-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_comentario_data'),
        ('avaliacoes', '0001_initial'),
        ('pontosturisticos', '0002_pontosturisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.avalicao'),
        ),
        migrations.AddField(
            model_name='pontosturisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.comentario'),
        ),
    ]
