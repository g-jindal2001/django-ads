from django.db import models
#http://jtdz-solenoids.com/stackoverflow_/questions/57500482/python-django-associating-a-foreignkey-on-users-integrityerror-not-null-const

class Category(models.Model) :
    name = models.CharField(max_length=128)


    def __str__(self) :
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128) #0
    description = models.CharField(max_length=512, null=True)
    justification = models.CharField(max_length=512, null=True)
    year = models.IntegerField(null=True) #1
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.CharField(max_length=128, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    def __str__(self) :
        return self.name