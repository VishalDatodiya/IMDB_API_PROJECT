# Generated by Django 4.1.5 on 2023-01-07 18:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_remove_review_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='watchlist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='watchlist_app.watchlist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
