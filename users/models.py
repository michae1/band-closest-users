from django.db import models

# Create your models here.
class SocialGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    social_id = models.IntegerField(null=True, blank=True)
    processed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("%s"%(self.name))

class SocialUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.IntegerField(null=True, blank=True)
    city_name = models.CharField(max_length=255)
    city_id = models.IntegerField(null=True, blank=True)
    social_id = models.IntegerField(null=True, blank=True)
    country_name = models.CharField(max_length=255)
    country_id = models.IntegerField(null=True, blank=True)
    social_groups = models.ManyToManyField(SocialGroup)    