# Generated by Django 3.1.7 on 2021-03-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_transactions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='Account_no',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
