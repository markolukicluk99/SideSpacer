# Generated by Django 2.1.1 on 2018-11-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='locations/%Y/%m/%D'),
        ),
    ]