# Generated by Django 4.1.5 on 2023-01-07 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamplateform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StreamPlateform',
            new_name='StreamPlatform',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
    ]
