# Generated by Django 4.2.3 on 2023-07-18 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('CEDULA DE CIUDADANIA', 'Cc'), ('TARJETA DE IDENTIDAD', 'Td')], default='CEDULA DE CIUDADANIA', max_length=100)),
                ('document', models.CharField(max_length=100, unique=True)),
                ('names', models.CharField(max_length=100)),
                ('last_names', models.CharField(max_length=100)),
                ('hobbie', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
