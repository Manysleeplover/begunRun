# Generated by Django 3.1.3 on 2020-12-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]