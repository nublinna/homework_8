class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def car_engine(self):
        print("Автомобиль запущен")

    def car_info(self):
        print(f"Информация о машине:"
                f"\nЦвет: {self.color}"
                f"\nМодель: {self.type}"
                f"\nГод выпуска: {self.year}")

    def car_off(self):
        print("Автомобиль заглушен\n")


car_one = Car(color="красный", type="Tesla Model S", year=2019)
car_one.car_engine()
car_one.car_info()
car_one.car_off()

car_two = Car(color="Черный", type="Volkswagen Polo", year=2015)
car_two.car_engine()
car_two.car_info()
car_two.car_off()