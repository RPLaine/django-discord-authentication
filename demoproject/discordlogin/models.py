from django.db import models

class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    discord_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    discriminator = models.CharField(max_length=255)
    public_flags = models.IntegerField()
    premium_type = models.IntegerField()
    flags = models.IntegerField()
    banner = models.CharField(max_length=255)
    accent_color = models.CharField(max_length=255)
    global_name = models.CharField(max_length=255)
    avatar_decoration_data = models.CharField(max_length=255)
    banner_color = models.CharField(max_length=255)
    mfa_enabled = models.BooleanField()
    locale = models.CharField(max_length=255)