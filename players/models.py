from django.db import models


# Create your models here.
class GameGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    bgg_username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    groups = models.ManyToManyField(GameGroup, related_name="members", blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
