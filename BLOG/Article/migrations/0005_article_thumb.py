# Generated by Django 4.0.4 on 2022-04-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_remove_article_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='hhh.jpg', upload_to=''),
        ),
    ]
