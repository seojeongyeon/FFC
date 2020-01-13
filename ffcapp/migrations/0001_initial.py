# Generated by Django 2.2.7 on 2020-01-12 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('phonenumber', models.CharField(max_length=20)),
                ('start_time', models.TimeField(verbose_name='start_time')),
                ('end_time', models.TimeField(verbose_name='end_time')),
                ('holiday', models.CharField(max_length=27)),
                ('content', models.TextField()),
                ('menu', models.ImageField(blank=True, default='', upload_to='images/')),
                ('socket', models.CharField(choices=[('yes', '있음'), ('no', '없음'), ('soso', '적당히 있음')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', upload_to='images/')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ffcapp.Cafe')),
            ],
        ),
    ]
