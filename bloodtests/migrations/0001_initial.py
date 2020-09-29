# Generated by Django 2.2.14 on 2020-09-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodtests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=10)),
                ('lower', models.FloatField(null=True)),
                ('upper', models.FloatField(null=True)),
            ],
        ),
    ]