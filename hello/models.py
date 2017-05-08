from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Nationalities(models.Model):
    nationality = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nationality

    def __str__(self):
        return self.nationality

'''
class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.ForeignKey('Nationalities')

    def __unicode__(self):
        return self.name + " " + self.surname

    def __str__(self):
        return self.name + " " + self.surname
'''

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # The additional attributes we wish to include.
    nationality = models.CharField(max_length=20)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username