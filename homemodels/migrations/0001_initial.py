# Generated by Django 4.0 on 2021-12-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prodcatglist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catg', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('rank', models.SmallIntegerField()),
            ],
        ),
    ]
