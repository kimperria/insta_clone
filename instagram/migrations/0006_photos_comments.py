# Generated by Django 4.0.3 on 2022-04-03 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_rename_comment_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instagram.comments'),
            preserve_default=False,
        ),
    ]
