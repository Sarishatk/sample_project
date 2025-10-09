from django.db import models


class Studentmodel(models.model):

    name = models.CharField(max_length=30)

    age = models.BigIntegerField(null = False)

    qualification = models.CharField(max_length=10)

# makemigration
# migrate




