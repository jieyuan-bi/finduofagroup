# Generated by Django 3.2.4 on 2021-06-18 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'courses_catalogue',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='courses.cataloguemodel')),
            ],
            options={
                'db_table': 'courses_subject',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='courses.subjectmodel')),
            ],
            options={
                'db_table': 'courses_class',
                'ordering': ('name',),
            },
        ),
    ]
