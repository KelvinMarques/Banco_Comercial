# Generated by Django 4.2.7 on 2023-11-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=16)),
                ('titular', models.CharField(max_length=255)),
                ('data_vencimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CartaoDebito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=16)),
                ('titular', models.CharField(max_length=255)),
                ('data_vencimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao1', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacao1', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]