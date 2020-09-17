#import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

from imagekit.models import ImageSpecField

def image_upload_to(self, filename):
    self.original_filename = filename
    #uid = str(uuid.uuid4())
    extension = filename.split(".")[-1].lower()
    return f'user_profile/{self.pk}-{self.first_name}-avatar.{extension}'

#class Skill(models.Model):
#    name = models.CharField(_("Skill Name"), blank=True, max_length=30, default='')
#    value = models.PositiveIntegerField(
#        validators=[
#            MinValueValidator(0),
#            MaxValueValidator(100)
#        ], default=0
#    )

    def __str__(self):
        return self.name

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    first_name = models.CharField(_("User First Name"), blank=True, max_length=120, default='')
    last_name = models.CharField(_("User Last Name"), blank=True, max_length=120, default='')
    avatar = models.ImageField(upload_to=image_upload_to, default = 'img/default.png', blank=True)
    original_filename = models.CharField(max_length=500, default='')
#    skills = models.ManyToManyField('Skill', blank=True, verbose_name='skills')
    title = models.CharField(_("User Title"), blank=True, max_length=160, default='')
    birth_date = models.DateTimeField(_("User Birth_date"), null=True, blank=True, editable=False)
    city = models.CharField(_("User City"), max_length=255, default='')
    state = models.CharField(_("User State"), max_length=255, default='')
    country = models.CharField(_("User Country"), max_length=255, default='')

    thumbnail = ImageSpecField(source="avatar", id="users:avatar:thumbnail")
    list_thumbnail = ImageSpecField(source="avatar", id="users:avatar:list_thumbnail")
    small_thumbnail = ImageSpecField(source="avatar", id="users:avatar:small_thumbnail")
    medium_thumbnail = ImageSpecField(source="avatar", id="users:avatar:medium_thumbnail")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def get_age(self):
        return self.bird_date

    @property
    def get_avatar(self):
        return self.avatar.url #or f'{settings.STATIC_URL}/static/img/default.png'

#class Profile(models.Model): 
#    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
#                                on_delete=models.CASCADE,
#                                primary_key=True)