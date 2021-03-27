from .models import Todo


def find_odom(car, snaps):
    car_snaps = snaps.filter(car=car.id).order_by("-mileage")
    if len(car_snaps) == 0:
        print("We really shouldn't have cars without mileage")
        return 0
    return car_snaps[0].mileage


def create_defaults(user, car, snaps):
    base_mileage = find_odom(car, snaps)

    def get_due_mileage(interval):
        if interval > base_mileage:
            # it's safe to assume that the user has not done this task
            return interval
        else:
            return base_mileage + interval

    defaults = [
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

    for t in defaults:
        t.save()
