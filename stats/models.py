from django.db import models
import uuid


class Vehicle(models.Model):
    """
    Representation of a polestar vehicle to store journey statistics against
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000, help_text='A nick name for your vehicle')
    vin_number = models.CharField(max_length=17, help_text='Vehicle identification number')
    # Eventually we will link this to a user account... but not todays


class Journey(models.Model):
    """
    A single journey as described by a polestar log file
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Eventually force requirement for vehicle, but in testing we allow null/blank
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_address = models.CharField(max_length=5000)
    end_address = models.CharField(max_length=5000)
    distance = models.FloatField()
    energy_consumption = models.FloatField()
    category = models.CharField(max_length=200)
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    end_latitude = models.FloatField()
    end_longitude = models.FloatField()
 