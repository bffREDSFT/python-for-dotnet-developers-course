from typing import List

from models.basic_car import BasicCar
from models.car import Car
from models.sports_car import SportsCar
from models.electric_car import ElectricCar     


def main():
    cars = create_cars()
    for car in cars:
        car.drive()
        car.refuel()

        print()


def create_cars() -> List[Car]:
    return [
        SportsCar('BMW','gasolina', 8, 50_000),
        BasicCar('Mercedes','gasolina', 6, 60_000),
        ElectricCar('Tesla', 80_000),
        ElectricCar('Toyota', 30_000),
    ]

if __name__ == '__main__':
    main()