# Generated by Django 3.2 on 2021-04-11 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20210411_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]
