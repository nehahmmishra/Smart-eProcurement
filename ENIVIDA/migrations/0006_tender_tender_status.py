# Generated by Django 4.1 on 2022-08-10 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0005_tender_tender_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='Tender_Status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ENIVIDA.status'),
            preserve_default=False,
        ),
    ]