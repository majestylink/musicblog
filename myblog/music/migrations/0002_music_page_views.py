# Generated by Django 3.1.2 on 2020-10-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
    ]
