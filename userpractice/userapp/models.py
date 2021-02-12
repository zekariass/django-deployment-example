from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileData(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE,)
    user_portfolio = models.URLField(blank=True)
    user_profile_pic = models.ImageField(upload_to = 'profile_imgs',blank=True)

    def __str__(self):
        return self.user.username
