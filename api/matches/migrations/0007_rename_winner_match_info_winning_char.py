# Generated by Django 4.0.2 on 2022-02-16 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_alter_match_info_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match_info',
            old_name='winner',
            new_name='winning_char',
        ),
    ]
