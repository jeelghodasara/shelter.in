# Generated by Django 3.1.5 on 2021-03-28 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_city', models.CharField(blank=True, choices=[('Rajkot', 'Rajkot'), ('Ahmedabad', 'Ahmedabad'), ('Vadodara', 'Vadodara')], max_length=50, null=True)),
                ('p_state', models.CharField(choices=[('Gujarat', 'Gujarat'), ('Rajasthan', 'Rajasthan'), ('Panjab', 'Panjab'), ('Hariyana', 'Hariyana')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('area_code', models.IntegerField(default=91)),
                ('phone', models.CharField(max_length=12)),
                ('p_type', models.CharField(choices=[('PG', 'PG'), ('Apartment', 'Apartment')], max_length=50)),
                ('p_address', models.CharField(max_length=1024)),
                ('execting_cus', models.BooleanField(default=False)),
                ('p_price', models.IntegerField(default=0)),
                ('p_time_area', models.CharField(max_length=50)),
                ('p_rooms_available', models.IntegerField(default=1)),
                ('p_floor_no', models.IntegerField(default=0)),
                ('p_sharing_member', models.IntegerField(default=1)),
                ('tenants_preffered', models.CharField(choices=[('Boys', 'Boys'), ('Girls', 'Girls'), ('Family', 'Family')], max_length=50)),
                ('photo', models.ImageField(null=True, upload_to='p_images')),
                ('p_amanities', models.CharField(max_length=200)),
                ('house_rules', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.user_registration')),
            ],
        ),
    ]
