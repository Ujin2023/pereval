# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from email.policy import default

from django.db import models

class Users(models.Model):
    email = models.TextField(unique=True)
    fam = models.TextField()
    name = models.TextField()
    otc = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'users'

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    class Meta:
        db_table = 'coords'

class Images(models.Model):
    title = models.TextField(blank=True, null=True)
    img = models.BinaryField()
    date_added = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'images'

class PerevalAdded(models.Model):
    NEW = 'new'
    CHECKING = 'checking'
    ACCEPTED = 'accepted'

    STATUS_CHOICES = [
        (NEW, 'Новый'),
        (CHECKING, 'В работе'),
        (ACCEPTED, 'Принят'),
    ]

    date_added = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    beauty_title = models.TextField(blank=True, null=True)
    title = models.TextField()
    other_titles = models.TextField(blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    coord = models.ForeignKey(Coords, on_delete=models.CASCADE, blank=True, null=True)
    level_winter = models.TextField(blank=True, null=True)
    level_summer = models.TextField(blank=True, null=True)
    level_autumn = models.TextField(blank=True, null=True)
    level_spring = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=NEW)
    images = models.ManyToManyField(Images, through='PerevalImages', blank=True, null=True)
    class Meta:
        db_table = 'pereval_added'


class PerevalImages(models.Model):
    pereval_id= models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pereval_images'



