# Generated by Django 3.1.3 on 2020-12-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=7, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(null=True, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='Фотография профиля'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_description',
            field=models.CharField(max_length=300, null=True, verbose_name='Описание профиля'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(null=True, verbose_name='Вес'),
        ),
    ]
