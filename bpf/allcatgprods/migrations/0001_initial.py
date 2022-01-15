# Generated by Django 4.0 on 2021-12-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='top_stock_trading_and_investments_apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='User Rating')),
                ('pros', models.TextField(max_length=500, verbose_name="Enter Pros (using'/'to seperate)")),
                ('cons', models.TextField(max_length=500, verbose_name="Enter Cons (using'/'to seperate)")),
                ('upr', models.TextField(verbose_name="Users +ve review(using'/'to seperate)")),
                ('unr', models.TextField(verbose_name="Users -ve review(using'/'to seperate)")),
                ('youtubelink', models.URLField(verbose_name='Youtube Reveiw/Comparision link')),
                ('rank', models.PositiveSmallIntegerField(verbose_name='App Rank')),
                ('appname', models.CharField(max_length=50, verbose_name='Name of App')),
                ('aoc', models.PositiveSmallIntegerField(verbose_name='Account opening charge')),
                ('amc', models.PositiveSmallIntegerField(verbose_name='Account maintenance charge')),
                ('edc', models.CharField(max_length=50, verbose_name='Equity Delivery Charges')),
                ('idc', models.CharField(max_length=50, verbose_name='Intraday Charges')),
                ('fc', models.CharField(max_length=50, verbose_name='Future Charges')),
                ('oc', models.CharField(max_length=50, verbose_name='Option Charges')),
                ('dpc', models.CharField(max_length=50, verbose_name='DP charge')),
                ('est', models.PositiveSmallIntegerField(verbose_name='Establishment Year')),
                ('calc', models.URLField(verbose_name='Brokerage Calculator Link')),
                ('applink', models.URLField(verbose_name='App/Website link')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
