# Generated by Django 3.2 on 2022-11-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
