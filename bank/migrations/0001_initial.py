# Generated by Django 3.1.7 on 2021-03-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Account_no', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
    ]
