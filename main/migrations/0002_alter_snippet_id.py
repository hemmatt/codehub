# Generated by Django 3.2.9 on 2021-11-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='id',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
