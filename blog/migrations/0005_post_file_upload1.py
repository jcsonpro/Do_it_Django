# Generated by Django 4.1 on 2023-02-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="file_upload1",
            field=models.FileField(blank=True, upload_to="blog/files/%Y/%m/%d/"),
        ),
    ]
