# Generated by Django 4.2.3 on 2024-12-01 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animais', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarioEntrada', models.DateTimeField()),
                ('horarioSaida', models.DateTimeField()),
                ('tipoServico', models.CharField(choices=[('banho', 'Banho'), ('tosa', 'Tosa'), ('banho e tosa', 'Banho e Tosa')], max_length=50)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animais.animal')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
            options={
                'verbose_name': 'ServicoPet',
                'verbose_name_plural': 'ServicosPet',
            },
        ),
    ]
