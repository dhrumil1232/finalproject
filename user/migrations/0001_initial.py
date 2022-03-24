# Generated by Django 4.0.3 on 2022-03-23 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField()),
                ('role', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Usermaster',
            },
        ),
        migrations.CreateModel(
            name='Housekeeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='housekeeper_img')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermaster')),
            ],
            options={
                'db_table': 'Housekeeper',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermaster')),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
    ]
