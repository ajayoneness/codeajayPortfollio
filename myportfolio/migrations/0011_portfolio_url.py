# Generated by Django 4.2.1 on 2023-07-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0010_alter_portfolio_fulldecription'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]