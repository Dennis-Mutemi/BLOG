# Generated by Django 4.0.4 on 2022-04-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='defaut.png', upload_to=''),
        ),
    ]
