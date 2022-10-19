from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Person(models.Model):

    ID = models.IntegerField(help_text="Person ID", unique=True, primary_key=True, default=0)
    forename = models.CharField(max_length=20, help_text="Forename / given name")
    surname = models.CharField(max_length=30, help_text="Surname")
    parent_id = ArrayField(models.IntegerField(), blank=True, null=True, help_text="Parent ID list")
    user = models.OneToOneField(User, models.SET_NULL, blank=True, null=True)

    def name(self, use_middle_names=True, use_maiden_name=False):
        """Returns the full name"""
        name = " ".join([self.forename, self.surname])
        return name

    def __str__(self):
        return self.name()

    def __repr__(self):
        return self.name()

    class Meta:
        ordering = ["ID", "surname", "forename", "parent_id"]
