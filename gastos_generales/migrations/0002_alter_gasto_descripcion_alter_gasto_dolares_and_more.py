# Generated by Django 5.2.4 on 2025-07-19 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos_generales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='dolares',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='soles',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='sustento',
            field=models.FileField(blank=True, null=True, upload_to='files/gastos_generales/'),
        ),
    ]
