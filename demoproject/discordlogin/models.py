from django.db import models

class OldUserData(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)

class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    discord_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255, blank=True, null=True)
    public_flags = models.IntegerField()
    premium_type = models.IntegerField()
    flags = models.IntegerField()
    banner = models.CharField(max_length=255, blank=True, null=True)
    accent_color = models.CharField(max_length=255, blank=True, null=True)
    global_name = models.CharField(max_length=255, blank=True)
    avatar_decoration_data = models.CharField(max_length=255, blank=True, null=True)
    banner_color = models.CharField(max_length=255, blank=True, null=True)
    mfa_enabled = models.BooleanField()
    locale = models.CharField(max_length=255)
    nmid = models.ForeignKey(OldUserData, on_delete=models.CASCADE, to_field='id', blank=True, null=True)