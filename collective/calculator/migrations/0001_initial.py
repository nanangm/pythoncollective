# Generated by Django 3.2.3 on 2021-05-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calculator',
            fields=[
                ('calculation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=15)),
                ('second', models.CharField(max_length=15)),
                ('operator', models.CharField(max_length=15)),
                ('result', models.CharField(max_length=15)),
            ],
        ),
    ]
