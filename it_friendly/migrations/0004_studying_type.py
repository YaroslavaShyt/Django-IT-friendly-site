# Generated by Django 4.2 on 2023-04-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_friendly', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studying',
            name='type',
            field=models.CharField(default='value', max_length=100),
            preserve_default=False,
        ),
    ]
