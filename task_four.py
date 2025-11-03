class Sphere:
    def __init__(self, radius=None, cord_x=None, cord_y=None, cord_z=None):
        if radius is None and cord_x is None and cord_y is None and cord_z is None:
            self.radius = 1
            self.cord_x = 0
            self.cord_y = 0
            self.cord_z = 0
        elif cord_x is None and cord_y is None and cord_z is None:
            self.radius = radius
            self.cord_x = 0
            self.cord_y = 0
            self.cord_z = 0
        else:
            self.radius = radius
            self.cord_x = cord_x
            self.cord_y = cord_y
            self.cord_z = cord_z

    def get_volume(self):
        return (4 / 3) * 3.14 * (self.radius ** 3)

    def get_square(self):
        return 4 * 3.14 * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.cord_x, self.cord_y, self.cord_z

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.cord_x = x
        self.cord_y = y
        self.cord_z = z

    def is_point_inside(self, x, y, z):
        dist_x = x - self.cord_x
        dist_y = y - self.cord_y
        dist_z = z - self.cord_z

        square_x = dist_x * dist_x
        square_y = dist_y * dist_y
        square_z = dist_z * dist_z

        summ = square_x + square_y + square_z

        distance = summ ** 0.5

        if distance <= self.radius:
            return True
        else:
            return False


while True:
    user_input = input("Выберите режим программы:"
                  "\n1 -- Сфера с пользовательским вводом"
                  "\n2 -- Сфера без заданных координат"
                  "\n3 -- Сфера с пользовательским радиусом"
                  "\n4 -- Выход из программы: ")

    if user_input == "1":
        print("\nСфера с пользовательским вводом")
        while True:
            radius = input("Введите радиус: ")
            if radius.isdigit():
                radius = int(radius)
                break
            else:
                print("Введите целое число!")

        while True:
            cord_x = input("Введите первую координату центра сферы: ")
            if cord_x.isdigit():
                cord_x = int(cord_x)
                break
            else:
                print("Введите целое число!")

        while True:
            cord_y = input("Введите вторую координату центра сферы: ")
            if cord_y.isdigit():
                cord_y = int(cord_y)
                break
            else:
                print("Введите целое число!")

        while True:
            cord_z = input("Введите третью координату центра сферы: ")
            if cord_z.isdigit():
                cord_z = int(cord_z)
                break
            else:
                print("Введите целое число!")

        sphere_one = Sphere(radius, cord_x, cord_y, cord_z)
        print(f"Объем шара: {sphere_one.get_volume()}")
        print(f"Площадь внешней сферы поверхности шара: {sphere_one.get_square()}")
        print(f"Радиус сферы: {sphere_one.get_radius()}")
        print(f"Координаты центра: {sphere_one.get_center()}")

        while True:
            x = input("Введите координату x: ")
            if x.isdigit():
                x = int(x)
                break
            else:
                print("Введите целое число!")

        while True:
            y = input("Введите координату y: ")
            if y.isdigit():
                y = int(y)
                break
            else:
                print("Введите целое число!")

        while True:
            z = input("Введите координату z: ")
            if z.isdigit():
                z = int(z)
                break
            else:
                print("Введите целое число!")

        print(f"Находится ли точка внутри сферы: {sphere_one.is_point_inside(x, y, z)}")

    if user_input == "2":
        print("\nСфера без заданных координат")
        sphere_two = Sphere()
        print(f"Радиус сферы: {sphere_two.radius}"
              f"\nКоординаты центра сферы: {sphere_two.cord_x}, {sphere_two.cord_y}, {sphere_two.cord_z}")
        print(f"Объем шара: {sphere_two.get_volume()}")
        print(f"Площадь внешней сферы поверхности шара: {sphere_two.get_square()}")
        print(f"Радиус сферы: {sphere_two.get_radius()}")
        print(f"Координаты центра: {sphere_two.get_center()}")

        while True:
            x = input("Введите координату x: ")
            if x.isdigit():
                x = int(x)
                break
            else:
                print("Введите целое число!")

        while True:
            y = input("Введите координату y: ")
            if y.isdigit():
                y = int(y)
                break
            else:
                print("Введите целое число!")

        while True:
            z = input("Введите координату z: ")
            if z.isdigit():
                z = int(z)
                break
            else:
                print("Введите целое число!")

        print(f"Находится ли точка внутри сферы: {sphere_two.is_point_inside(x, y, z)}")

    if user_input == "3":
        print("\nСфера с пользовательским радиусом")
        while True:
            radius = input("Введите радиус: ")
            if radius.isdigit():
                radius = int(radius)
                break
            else:
                print("Введите целое число!")

        sphere_three = Sphere(radius)
        print(f"Объем шара: {sphere_three.get_volume()}")
        print(f"Площадь внешней сферы поверхности шара: {sphere_three.get_square()}")
        print(f"Радиус сферы: {sphere_three.get_radius()}")
        print(f"Координаты центра: {sphere_three.get_center()}")

        while True:
            x = input("Введите координату x: ")
            if x.isdigit():
                x = int(x)
                break
            else:
                print("Введите целое число!")

        while True:
            y = input("Введите координату y: ")
            if y.isdigit():
                y = int(y)
                break
            else:
                print("Введите целое число!")

        while True:
            z = input("Введите координату z: ")
            if z.isdigit():
                z = int(z)
                break
            else:
                print("Введите целое число!")

        print(f"Находится ли точка внутри сферы: {sphere_three.is_point_inside(x, y, z)}")

    if user_input == "4":
        break