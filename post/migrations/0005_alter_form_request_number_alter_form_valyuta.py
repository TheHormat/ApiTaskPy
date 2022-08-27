# Generated by Django 4.0.5 on 2022-08-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_form_color_form_request_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='request_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Sorğu nömrəsi'),
        ),
        migrations.AlterField(
            model_name='form',
            name='valyuta',
            field=models.CharField(blank=True, choices=[('azn', 'AZN'), ('usd', 'USD'), ('eur', 'EUR'), ('try', 'TRY'), ('rub', 'RUB')], default='azn', max_length=5, null=True, verbose_name='Valyuta'),
        ),
    ]