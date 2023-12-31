# Generated by Django 5.0 on 2024-01-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='accent_color',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='avatar',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='avatar_decoration_data',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='banner',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='banner_color',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='discriminator',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='global_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
