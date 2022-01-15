# Generated by Django 4.0 on 2022-01-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcatgprods', '0011_remove_mobile_bb_mobile_battery_mobile_memory'),
    ]

    operations = [
        migrations.CreateModel(
            name='camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Product')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='User Rating')),
                ('pros', models.TextField(max_length=500, verbose_name="Enter Pros (using'/'to seperate)")),
                ('cons', models.TextField(max_length=500, verbose_name="Enter Cons (using'/'to seperate)")),
                ('upr', models.TextField(verbose_name="Users +ve review(using'/'to seperate)")),
                ('unr', models.TextField(verbose_name="Users -ve review(using'/'to seperate)")),
                ('youtubelink', models.URLField(verbose_name='Youtube Reveiw/Comparision link')),
                ('amazonp', models.CharField(max_length=40, verbose_name='Price on Amazon')),
                ('amazonlink', models.URLField(verbose_name='Amazon Link')),
                ('flipkartp', models.CharField(max_length=40, verbose_name='Price on Flipkart')),
                ('flipkartlink', models.URLField(verbose_name='Flipkart link')),
                ('officialp', models.CharField(max_length=40, verbose_name='Price on Official store')),
                ('officiallink', models.URLField(verbose_name='Official link')),
                ('minp', models.PositiveIntegerField(verbose_name='Minimum Price')),
                ('minplink', models.URLField(verbose_name='Minimum Price Link')),
                ('minpseller', models.CharField(max_length=50, verbose_name='Minimum Price Seller')),
                ('rank', models.PositiveSmallIntegerField(verbose_name='Rank of product')),
                ('model', models.CharField(max_length=30, verbose_name='Model No.')),
                ('battery', models.CharField(max_length=100, verbose_name='Battery details')),
                ('dispsize', models.CharField(max_length=50, verbose_name='Display Size')),
                ('dim', models.CharField(max_length=200, verbose_name='Product Dimension')),
                ('pixel', models.CharField(max_length=100, verbose_name='Optical res(in pixel)')),
                ('mountinghardware', models.CharField(max_length=400, verbose_name='Mounting Hardware(In the box)')),
                ('shutterspeed', models.CharField(max_length=100, verbose_name='Minimum Shutter speed')),
                ('focallength', models.CharField(max_length=100, verbose_name='Minimum Focal length')),
                ('fps', models.CharField(max_length=100, verbose_name='Continuos shooting speed(in fps)')),
                ('prodimg', models.ImageField(default='defaultimg/', upload_to='e_commerce/camera/img/', verbose_name='Product image')),
                ('warrenty', models.CharField(max_length=100, verbose_name='Warrenty')),
                ('reliancep', models.CharField(max_length=40, verbose_name='Price on Reliance Digital')),
                ('reliancelink', models.URLField(verbose_name='Reliance Link')),
                ('spclcatg', models.CharField(max_length=100, verbose_name='Special Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]