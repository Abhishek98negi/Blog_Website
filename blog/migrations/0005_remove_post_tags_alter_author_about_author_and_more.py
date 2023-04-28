# Generated by Django 4.1 on 2023-04-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='author',
            name='about_author',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]