# Generated by Django 3.1.14 on 2021-12-30 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211230_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.message'),
        ),
    ]
