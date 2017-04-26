from django.db import models

# Create your models here.

class Nationalities(models.Model):
    nationality = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nationality

    def __str__(self):
        return self.nationality

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.ForeignKey('Nationalities')

    def __unicode__(self):
        return self.name + " " + self.surname

    def __str__(self):
        return self.name + " " + self.surname
