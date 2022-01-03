from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name


class Owner(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Animal(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    comments = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
