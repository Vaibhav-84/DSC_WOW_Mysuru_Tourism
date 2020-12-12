# Generated by Django 3.1.4 on 2020-12-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valo',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
