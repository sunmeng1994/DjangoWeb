# Generated by Django 2.2.2 on 2019-07-12 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_txt',
            new_name='choice_text',
        ),
    ]
