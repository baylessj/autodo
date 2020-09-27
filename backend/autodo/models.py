"""Defines the types of objects created and used by the user."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class OdomSnapshot(models.Model):
    """The relevant data for an update to a car's odometer reading."""

    car = models.ForeignKey(
        "Car", null=True, related_name="snaps", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        "User", related_name="odomSnapshot", on_delete=models.CASCADE
    )

    date = models.DateTimeField()
    mileage = models.FloatField()

    def __str__(self):
        return "Odometer Snapshot for car: {} on: {} at: {}".format(
            self.car, self.date, self.mileage
        )

    class Meta:
        ordering = ["-mileage"]


def sortedOdomSnaps(carId):
    return OdomSnapshot.objects.filter(car=carId).order_by("-date", "-mileage")


def find_odom(obj):
    odomSnaps = sortedOdomSnaps(obj.id)
    try:
        mileage = odomSnaps[0].mileage
        print(f"here: {mileage}")
        return mileage
    except:
        return 0


class Todo(models.Model):
    """A task or action to perform on a car."""

    owner = models.ForeignKey("User", related_name="todo", on_delete=models.CASCADE)
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    completionOdomSnapshot = models.ForeignKey(
        "OdomSnapshot", on_delete=models.SET_NULL, blank=True, null=True
    )

    name = models.CharField(max_length=32, null=False)
    dueMileage = models.FloatField(default=None, blank=True, null=True)
    dueDate = models.DateTimeField(default=None, blank=True, null=True)
    # TODO: calculate this on POST
    estimatedDueDate = models.BooleanField(default=False, blank=True, null=True)
    mileageRepeatInterval = models.FloatField(default=None, blank=True, null=True)
    daysRepeatInterval = models.IntegerField(default=None, blank=True, null=True)
    monthsRepeatInterval = models.IntegerField(default=None, blank=True, null=True)
    yearsRepeatInterval = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        ordering = ["dueDate", "dueMileage"]


def create_defaults(user, car):
    base_mileage = find_odom(car)
    print(base_mileage)
    print(OdomSnapshot.objects.filter(car=car.id))

    def get_due_mileage(interval):
        if interval > base_mileage:
            # it's safe to assume that the user has not done this task
            return interval
        else:
            return base_mileage + interval

    return [
        Todo(
            owner=user,
            car=car,
            name="Oil",
            dueMileage=get_due_mileage(3500),
            mileageRepeatInterval=3500,
        ),
        Todo(
            owner=user,
            car=car,
            name="Tire Rotation",
            dueMileage=get_due_mileage(7500),
            mileageRepeatInterval=7500,
        ),
        Todo(
            owner=user,
            car=car,
            name="Engine Filter",
            dueMileage=get_due_mileage(45000),
            mileageRepeatInterval=45000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Wiper Blades",
            dueMileage=get_due_mileage(30000),
            mileageRepeatInterval=30000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Alignment Check",
            dueMileage=get_due_mileage(40000),
            mileageRepeatInterval=40000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Cabin Filter",
            dueMileage=get_due_mileage(45000),
            mileageRepeatInterval=45000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Tires",
            dueMileage=get_due_mileage(50000),
            mileageRepeatInterval=50000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Brakes",
            dueMileage=get_due_mileage(60000),
            mileageRepeatInterval=60000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Spark Plugs",
            dueMileage=get_due_mileage(60000),
            mileageRepeatInterval=60000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Front Struts",
            dueMileage=get_due_mileage(75000),
            mileageRepeatInterval=75000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Rear Struts",
            dueMileage=get_due_mileage(75000),
            mileageRepeatInterval=75000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Battery",
            dueMileage=get_due_mileage(75000),
            mileageRepeatInterval=75000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Serpentine Belt",
            dueMileage=get_due_mileage(150000),
            mileageRepeatInterval=150000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Transmission Fluid",
            dueMileage=get_due_mileage(100000),
            mileageRepeatInterval=100000,
        ),
        Todo(
            owner=user,
            car=car,
            name="Coolant Change",
            dueMileage=get_due_mileage(100000),
            mileageRepeatInterval=100000,
        ),
    ]


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"


class Car(models.Model):
    """Represents the data for a Car type."""

    owner = models.ForeignKey(User, related_name="car", on_delete=models.CASCADE)

    name = models.CharField(max_length=32, null=False)
    make = models.CharField(max_length=32, blank=True, null=True)
    model = models.CharField(max_length=32, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    vin = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to="cars", null=True)
    color = models.IntegerField(default=128)  # TODO: autodo green to int maybe?

    def __str__(self):
        return "Car named: {}".format(self.name)


class Refueling(models.Model):
    """Data associated with a car's refueling event."""

    owner = models.ForeignKey(User, related_name="refueling", on_delete=models.CASCADE)
    odomSnapshot = models.ForeignKey(OdomSnapshot, on_delete=models.CASCADE)

    cost = models.IntegerField()  # For USD, scale this up by x100 to get an int
    amount = models.FloatField()

    def __str__(self):
        return "Refueling for cost: {} and amount: {}".format(self.cost, self.amount)
