# Generated by Django 5.0.3 on 2024-03-26 14:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_team_options_rename_name_team_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_image/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Услуга 2',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
