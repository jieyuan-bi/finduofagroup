# Generated by Django 3.2.4 on 2021-06-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_classmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]
