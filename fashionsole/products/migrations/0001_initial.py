# Generated by Django 4.1.7 on 2023-05-06 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catimge', models.ImageField(upload_to='pic')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=100)),
                ('productname', models.TextField()),
                ('img', models.ImageField(upload_to='pic')),
                ('discprice', models.CharField(max_length=10)),
                ('disc', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=10)),
                ('size', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
