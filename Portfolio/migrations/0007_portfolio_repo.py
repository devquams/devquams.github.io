# Generated by Django 3.2.16 on 2023-01-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0006_remove_portfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='repo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
