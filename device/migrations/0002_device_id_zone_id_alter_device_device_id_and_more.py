# Generated by Django 4.2.1 on 2024-06-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zone',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
