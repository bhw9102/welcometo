# Generated by Django 2.1.5 on 2019-02-10 15:35

from django.db import migrations, models
import game.tools


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190208_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructionclass',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=game.tools.combine_file_path),
        ),
        migrations.AlterField(
            model_name='effectclass',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=game.tools.combine_file_path),
        ),
    ]