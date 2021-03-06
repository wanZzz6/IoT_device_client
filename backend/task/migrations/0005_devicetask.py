# Generated by Django 2.1.4 on 2019-06-05 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0008_auto_20190603_1057'),
        ('task', '0004_auto_20190605_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=20)),
                ('address', models.IntegerField()),
                ('function_name', models.CharField(max_length=20, null=True, verbose_name='功能名称')),
                ('identifier', models.CharField(max_length=10, verbose_name='标识符')),
                ('modbus_function_code', models.IntegerField(verbose_name='modbus功能码')),
                ('start_address', models.IntegerField()),
                ('data_length', models.IntegerField(default=16)),
                ('top_limit', models.FloatField(null=True)),
                ('low_limit', models.FloatField(null=True)),
                ('scale', models.FloatField(default=1, verbose_name='缩放因子')),
                ('interval', models.IntegerField(default=5, verbose_name='采集间隔（s）')),
                ('send_way', models.CharField(choices=[('change', '改变上报'), ('time', '定时上报')], max_length=6)),
                ('gateway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateway.GatewayBase')),
            ],
        ),
    ]
