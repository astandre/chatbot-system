from django.db import models
from nluengine.models import Intents


# Create your models here.


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    # id_oc = models.CharField(max_length=20, null=False, default=9999999999)
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    email = models.EmailField(blank=True)

    class Meta:
        default_related_name = 'users'
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = 'users'

    def __str__(self):
        return self.first_name + " " + self.last_name


class SocialNetworks(models.Model):
    id_account = models.CharField(max_length=10, null=False, default=9999999999)
    user_name = models.CharField(max_length=30, null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    FACEBOOK = 'F'
    TWITTER = 'T'
    TELEGRAM = 'TG'
    WEB = 'W'
    SN_CHOICES = (
        (TWITTER, 'Twitter'),
        (FACEBOOK, 'Facebook'),
        (TELEGRAM, 'Telegram'),
        (WEB, 'W')
    )
    social_network = models.CharField(
        max_length=2,
        choices=SN_CHOICES,
        default=TELEGRAM
    )

    class Meta:
        default_related_name = 'socialnetworks'
        verbose_name = "SocialNetwork"
        verbose_name_plural = "SocialNetworks"
        db_table = 'socialnetworks'

    def __str__(self):
        return self.user_name


class Inputs(models.Model):
    id_input = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(null=False, blank=True)
    text = models.CharField(max_length=400, null=False)
    location = models.CharField(max_length=200, null=False, blank=True)
    raw_input = models.CharField(max_length=3000, null=False, blank=True)
    social_network = models.ForeignKey(SocialNetworks, on_delete=models.CASCADE, null=True, blank=True)
    solved = models.BooleanField(default=False)
    intent = models.OneToOneField(Intents, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_related_name = 'inputs'
        verbose_name = "Input"
        verbose_name_plural = "Inputs"
        db_table = 'inputs'
        get_latest_by = "id_input"

    def __str__(self):
        return self.text
