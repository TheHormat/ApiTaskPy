# Generated by Django 4.0.5 on 2022-08-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_form_edv_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip kod'),
        ),
    ]