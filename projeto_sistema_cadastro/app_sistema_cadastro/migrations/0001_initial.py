# Generated by Django 4.2.3 on 2023-07-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ordens',
            fields=[
                ('id_ordem', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('responsavel', models.TextField(max_length=255)),
            ],
        ),
    ]
