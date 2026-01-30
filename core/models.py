from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Percentage (0–100)")

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.degree


class CertificationStat(models.Model):
    category = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return self.category
