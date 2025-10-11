from django.db import models


class Studentmodel(models.Model):

    name = models.CharField(max_length=30)

    age = models.BigIntegerField(null = False)

    qualification = models.CharField(max_length=10)

# makemigration >>>>> 
# migrate


class Employeemodel(models.Model):

    name = models.CharField(max_length=20)

    age = models.IntegerField()

    salary = models.IntegerField()

    role = models.CharField(max_length=20)

    email = models.CharField(max_length=20)

    place = models.CharField(max_length=20)

    experience = models.CharField(max_length=20)




class Product(models.Model):

    name = models.CharField(max_length= 20)

    categroy = models.CharField(max_length= 10)

    brand = models.CharField(max_length= 20)

    price = models.IntegerField()

    stock = models.IntegerField()

    rating = models.IntegerField()

    city = models.CharField(max_length=20)

    seller  = models.CharField(max_length=20)

    