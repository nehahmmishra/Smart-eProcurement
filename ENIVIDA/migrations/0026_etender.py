# Generated by Django 4.1 on 2022-08-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0025_tender_address_auth_tender_allow_nda_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='etender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bidder_Name', models.CharField(default=0, max_length=200)),
                ('Tender_ID', models.CharField(default=0, max_length=200)),
                ('Tender_Type', models.CharField(default=0, max_length=200)),
                ('Tender_Category', models.CharField(default=0, max_length=200)),
                ('Total_Projects_Worked', models.IntegerField(default=0)),
                ('Total_Success_Projects', models.IntegerField(default=0)),
                ('Organization_size', models.IntegerField(default=0)),
                ('Organization_established_Year', models.IntegerField(default=0)),
                ('Value_of_Last_Project', models.IntegerField(default=0)),
                ('Proposed_Cost_of_Project', models.IntegerField(default=0)),
            ],
        ),
    ]