# Generated by Django 3.0.1 on 2020-01-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0002_auto_20200126_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]