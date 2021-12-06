from django.db import models


class species(models.Model):
    Name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.Name


class owner(models.Model):
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=45)
    Created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.FirstName + " " + self.LastName


class animal(models.Model):
    Name = models.CharField(max_length=45)
    Age = models.IntegerField()
    Species = models.ForeignKey(species, on_delete=models.SET_NULL)
    Owner = models.ForeignKey(owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class reservation(models.Model):
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    Animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    Comments = models.TextField()
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
