from django.db import models

from register_hospital.models import Hospital


class Detail(models.Model):
    image = models.ImageField()
    type_choices = (('GOV', 'Government'), ('PR', 'Private'))
    cost_choices = (('H', 'High'), ('M', 'Medium'), ('L', 'Low'))
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    description = models.TextField(default="Text Here")
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    # total_no_doctor = models.IntegerField(null=False)
    type = models.CharField(max_length=10, choices=type_choices)
    speciality = models.CharField(max_length=50, null=False)
    working_days = models.CharField(max_length=10, null=False)
    working_hours = models.CharField(max_length=10, null=False)
    blood_bank_availability = models.BooleanField(default=False)
    avg_cost = models.CharField(default=0, max_length=10, choices=cost_choices)

    def __str__(self):
        return self.hospital.name


class Doctor(models.Model):
    image = models.ImageField()
    details = models.ForeignKey(Detail, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    qualification = models.CharField(max_length=100, null=False)
    speciality = models.CharField(max_length=100, null=False)
    timing_from = models.TimeField()
    timing_to = models.TimeField()
    availability_now = models.BooleanField(default=False)
    experience = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    details = models.ManyToManyField(Detail)
    tag = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.tag


class Review(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=500, null=False)
    comment = models.TextField()

    def __str__(self):
        return self.name
