# Generated by Django 4.1.7 on 2023-07-03 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subscrib',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='info.sub'),
        ),
    ]
