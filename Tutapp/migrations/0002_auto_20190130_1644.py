# Generated by Django 2.1.5 on 2019-01-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=models.ManyToManyField(related_name='employees', to='Tutapp.Departments'),
        ),
    ]