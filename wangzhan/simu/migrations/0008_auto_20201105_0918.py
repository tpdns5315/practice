# Generated by Django 3.1.2 on 2020-11-05 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simu', '0007_auto_20201105_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='simu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simu.simu'),
        ),
    ]