# Generated by Django 5.1.4 on 2024-12-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='version',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
