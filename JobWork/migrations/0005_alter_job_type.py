# Generated by Django 3.2.5 on 2021-12-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobWork', '0004_auto_20211213_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('1', 'Full time'), ('2', 'Internship')], max_length=10),
        ),
    ]
