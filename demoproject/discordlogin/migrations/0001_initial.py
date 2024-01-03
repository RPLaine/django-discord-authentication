# Generated by Django 5.0 on 2024-01-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discord_id', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255)),
                ('discriminator', models.CharField(max_length=255)),
                ('public_flags', models.IntegerField()),
                ('premium_type', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('banner', models.CharField(max_length=255)),
                ('accent_color', models.CharField(max_length=255)),
                ('global_name', models.CharField(max_length=255)),
                ('avatar_decoration_data', models.CharField(max_length=255)),
                ('banner_color', models.CharField(max_length=255)),
                ('mfa_enabled', models.BooleanField()),
                ('locale', models.CharField(max_length=255)),
            ],
        ),
    ]