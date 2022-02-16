# Generated by Django 4.0.2 on 2022-02-14 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0003_match_info_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_info',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True,default=None, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
