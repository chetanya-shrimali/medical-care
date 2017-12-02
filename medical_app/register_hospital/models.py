from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=500, null=False)
    phone_number = models.IntegerField(default=0, null=False)
    password = models.CharField(max_length=100, null=False)
    license_id = models.CharField(max_length=250, null=False)
    verification = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' -> ' + self.license_id
