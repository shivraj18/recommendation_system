# Generated by Django 4.0.4 on 2022-07-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_system', '0003_alter_book_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Height',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
