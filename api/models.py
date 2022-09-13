from django.db import models


class Data(models.Model):
    name=models.CharField(max_length=120)
    department=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    experience=models.CharField(max_length=120)