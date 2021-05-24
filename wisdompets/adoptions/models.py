from django.db import models


class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    # Many to Many field is used because we want each pet to have a vaccine as well, but optional
    vaccination = models.ManyToManyField('Vaccine', blank=True)
    

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # makes sure we aren't returning an object and instead a string
    def __str__(self):
        return self.name


