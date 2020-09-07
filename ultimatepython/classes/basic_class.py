from inspect import signature


class Car:
    """Basic definition of a car.

    A car is a good entity for defining with a class because it has state
    and methods associated with it. We start with a simple mental model
    of what a car is, so that we can start with core concepts associated
    with a class definition.
    """

    def __init__(self, make, model, year, miles):
        """Constructor logic."""
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def __repr__(self):
        """Formal representation for developers."""
        return f"<Car make={self.make} model={self.model} year={self.year}>"

    def __str__(self):
        """Informal representation for users."""
        return f"{self.make} {self.model} ({self.year})"

    def drive(self, rate_in_mph):
        """Drive car at a certain rate."""
        return f"{self} is driving at {rate_in_mph} MPH"


def main():
    # Create a car with the provided class constructor
    car = Car("Bumble", "Bee", 2000, 200000.0)

    # Formal and informal representations are not the same
    assert repr(car) != str(car)

    # Call a method on the class constructor
    assert car.drive(75) == "Bumble Bee (2000) is driving at 75 MPH"

    # As a reminder: everything in Python is an object! And that applies
    # to classes in the most interesting way - because they're not only
    # subclasses of object - they are also instances of object. This
    # means that we can modify the Car class at runtime, just like any
    # other piece of data we define in Python
    assert issubclass(Car, object)
    assert isinstance(Car, object)

    # To emphasize the idea that everything is an object, let's look at
    # the `drive` method in more detail
    driving = getattr(car, "drive")

    # The variable method is the same as the instance method
    assert driving == car.drive

    # The variable method is bound to the instance
    assert driving.__self__ == car

    # And there is only one parameter for `driving` because `__self__`
    # binding is implicit
    driving_params = signature(driving).parameters
    assert len(driving_params) == 1
    assert "rate_in_mph" in driving_params


if __name__ == "__main__":
    main()
