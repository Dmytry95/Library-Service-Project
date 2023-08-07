# Generated by Django 4.2.3 on 2023-07-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author', 'cover')},
        ),
    ]
