# Generated by Django 2.2 on 2019-12-18 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('bprice', models.FloatField()),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.RegisterModel')),
            ],
        ),
    ]
