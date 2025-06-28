from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import override


class StaffBase(AbstractUser):
    name = models.CharField( max_length=100, blank=True, null=True)
    age = models.IntegerField( blank=True, null=True)
    role = models.CharField( max_length=100, blank=True, null=True)


class Manager(StaffBase):
    department = models.CharField( max_length=100, blank=True, null=True)
    has_company_card = models.BooleanField( blank=True, null=True,default=True)


class Intern(StaffBase):
    mentor = models.ForeignKey("Manager", on_delete=models.CASCADE)
    internship_end = models.DateField( blank=True, null=True)

