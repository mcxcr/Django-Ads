# Generated by Django 4.0 on 2022-07-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='remark',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
