# Generated by Django 4.1.1 on 2022-11-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('preffered_name', models.CharField(max_length=64)),
                ('title_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.BigIntegerField()),
                ('contact_ext', models.BigIntegerField()),
                ('join_date', models.DateField()),
                ('join_date_format', models.CharField(max_length=64)),
            ],
        ),
    ]
