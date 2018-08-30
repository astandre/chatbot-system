from django.db import models
from nluengine.models import Intents

# Create your models here.

FACEBOOK = 'F'
TWITTER = 'T'
TELEGRAM = 'TG'
SN_CHOICES = (
    (TWITTER, 'Twitter'),
    (FACEBOOK, 'Facebook'),
    (TELEGRAM, 'Telegram')
)


class Inputs(models.Model):
    id_input = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(null=False, blank=True)
    text = models.CharField(max_length=400, null=False)
    location = models.CharField(max_length=200, null=False, blank=True)
    raw_input = models.CharField(max_length=3000, null=False, blank=True)
    solved = models.BooleanField(default=False)
    source = models.CharField(
        max_length=2,
        choices=SN_CHOICES,
        default=TELEGRAM
    )
    intent = models.OneToOneField(Intents, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_related_name = 'inputs'
        verbose_name = "Input"
        verbose_name_plural = "Inputs"
        db_table = 'inputs'

    def __str__(self):
        return self.text


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_number = models.CharField(max_length=20, null=False, unique=True, default=9999999999)
    id_oc = models.CharField(max_length=20, null=False, unique=True, default=9999999999)
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    inputs = models.ForeignKey(Inputs, on_delete=models.CASCADE, null=False, blank=True)

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
