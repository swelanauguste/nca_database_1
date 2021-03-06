# Generated by Django 3.2.7 on 2021-09-29 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='clients.location'),
        ),
        migrations.AddField(
            model_name='client',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
