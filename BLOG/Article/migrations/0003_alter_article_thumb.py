# Generated by Django 4.0.4 on 2022-04-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_article_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='hhh.jpg', upload_to=''),
        ),
    ]
