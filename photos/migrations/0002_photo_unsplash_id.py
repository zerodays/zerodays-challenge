# Generated by Django 3.2.6 on 2021-08-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='unsplash_id',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
    ]
