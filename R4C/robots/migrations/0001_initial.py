# Generated by Django 4.2.5 on 2023-10-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=5)),
                ('model', models.CharField(max_length=2)),
                ('version', models.CharField(max_length=2)),
                ('created', models.DateTimeField()),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
