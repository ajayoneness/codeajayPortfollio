# Generated by Django 4.2.1 on 2023-07-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0007_portfolio_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, unique=False),
        ),
    ]