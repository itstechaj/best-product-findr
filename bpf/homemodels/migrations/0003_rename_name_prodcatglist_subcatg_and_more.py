# Generated by Django 4.0 on 2021-12-30 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homemodels', '0002_prodcatglist_catgimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodcatglist',
            old_name='name',
            new_name='subcatg',
        ),
        migrations.RenameField(
            model_name='prodcatglist',
            old_name='catgimg',
            new_name='subcatgimg',
        ),
    ]
