# Generated by Django 4.0 on 2022-01-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcatgprods', '0022_remove_laptop_backlit_remove_laptop_cache_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='bb',
            field=models.CharField(max_length=100, verbose_name='Battery Backup'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='memory',
            field=models.CharField(max_length=100, verbose_name='Ram+SSD+cache'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='os',
            field=models.CharField(max_length=50, verbose_name='Operating system'),
        ),
    ]