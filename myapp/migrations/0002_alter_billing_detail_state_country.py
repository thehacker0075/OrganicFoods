# Generated by Django 4.0.3 on 2022-04-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_detail',
            name='state_country',
            field=models.CharField(choices=[('Gujarat', 'Gujarat'), ('Panjab', 'Panjab'), ('Rajasthan', 'Rajasthan'), ('Kerala', 'Kerala')], max_length=100),
        ),
    ]
