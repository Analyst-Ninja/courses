"""
Dataclasses example
"""

from dataclasses import dataclass
from enum import Enum, auto


class FuelType(Enum):
    """
    Enum class for fuel type
    """

    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


@dataclass(order=True)
class Vehicle:
    """
    Vehicle class
    """

    brand: str
    model: str
    color: str
    license_plate: str
    driven_miles: int = 0
    fuel_type: FuelType = FuelType.ELECTRIC

    def needs_maintenance(self, maintenance_miles: int) -> bool:
        """
        Method for checking if vehicle needs maintenance
        """
        return self.driven_miles > maintenance_miles


def main():
    v1 = Vehicle(
        brand="BMW",
        model="M5 Competition",
        color="Black",
        license_plate="polymath",
        driven_miles=1000,
        fuel_type=FuelType.PETROL,
    )
    v2 = Vehicle(
        brand="Maruti",
        model="Alto",
        color="Black",
        license_plate="polymath",
        driven_miles=1000000,
        fuel_type=FuelType.PETROL,
    )

    maintenance_miles = 100000

    print(v1.needs_maintenance(maintenance_miles))
    print(v2.needs_maintenance(maintenance_miles))

    print(v1)
    print(v2)


if __name__ == "__main__":
    main()
