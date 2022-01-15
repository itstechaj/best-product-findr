# Generated by Django 4.0 on 2022-01-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcatgprods', '0010_mobile_alter_laptop_amazonp_alter_laptop_flipkartp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='bb',
        ),
        migrations.AddField(
            model_name='mobile',
            name='battery',
            field=models.CharField(default=1, max_length=100, verbose_name='Battery Backup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mobile',
            name='memory',
            field=models.CharField(default=0, max_length=25, verbose_name='Memory'),
            preserve_default=False,
        ),
    ]