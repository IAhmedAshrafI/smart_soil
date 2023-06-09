# Generated by Django 4.2.1 on 2023-07-06 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_alter_zone_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.zone')),
            ],
        ),
    ]
