from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Organisation(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

#signals !! IMPORTANTS
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        Organisation.objects.create(owner=instance)

post_save.connect(post_user_created_signal, sender=User)
