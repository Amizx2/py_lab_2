import doctest


class Car:
    def __init__(self, model: str, year: int, fuel_level: float, fuel_tank_capacity: float):
        """
        Создание объекта автомобиля.

        :param model: Марка и модель автомобиля
        :param year: Год выпуска
        :param fuel_level: Уровень топлива в баке
        :param fuel_tank_capacity: Емкость топливного бака

        Пример:
        >>> car = Car("Nissan silvia s15", 2000, 50, 65)
        """
        if not isinstance(model, str):
            raise TypeError("Модель машины должна быть строкой")
        if not isinstance(year,
                          int) or year < 1885:  # В этом году появилась первая машина, следовательно раньше быть не может:
            raise TypeError("Год выпуска должен быть числом больше или равным 1885")

        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.fuel_tank_capacity = fuel_tank_capacity

    def drive(self, distance: float) -> str:
        """
        Поездка на указанное расстояние. Уменьшает уровень топлива.

        :param distance: Расстояние в километрах
        :return: Строка с информацией о поездке и оставшемся топливе
        :raise ValueError: Если расстояние отрицательное или недостаточно топлива
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")

        fuel_needed = distance * 0.1  # предположим, что расход топлива 10 литров на 100 км
        if fuel_needed > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки")

        self.fuel_level -= fuel_needed
        return f"Поездка на {distance} км. Осталось {self.fuel_level} литров топлива."

    def refuel(self, amount: float) -> None:
        """
        Заправка автомобиля топливом.

        :param amount: Количество топлива для заправки
        :raise ValueError: Если количество топлива больше, чем вместимость бака или меньше 0
        """
        if not isinstance(amount, (float, int)) or amount <= 0:
            raise ValueError('Количество топлива должно быть положительным числом')
        if self.fuel_level + amount > self.fuel_tank_capacity:
            raise ValueError("Заправка не может превысить объем бака")
        self.fuel_level += amount


if __name__ == "__main__":
    doctest.testmod()

    # Пример работы класса
    car = Car("Volkswagen Touareg", 2010, 50, 85)
    print("Топлива в баке: ", car.fuel_level)
    print(car.drive(100))  # Вызываем метод отдельно
    print("Осталось топлива: ", car.fuel_level)
    print("Заправка 20 литров")
    car.refuel(20)  # Заправляем 20 литров
    print("Новый уровень топлива: ", car.fuel_level)
    print(" ")

class Smartphone:
    def __init__(self, model: str, battery_level: float, battery_capacity: float):
        """
        Создание объекта смартфона.

        :param model: Модель смартфона
        :param battery_level: Уровень заряда батареи
        :param battery_capacity: Ёмкость батареи
        >>> phone = Smartphone("iPhone 12", 50, 100)
        """
        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть строкой")
        if not isinstance(battery_level, (int, float)) or battery_level < 0 or battery_level > battery_capacity:
            raise ValueError("Уровень заряда должен быть числом от 0 до емкости батареи")
        if not isinstance(battery_capacity, (int, float)) or battery_capacity <= 0:
            raise ValueError("Ёмкость батареи должна быть положительным числом")

        self.model = model
        self.battery_level = battery_level
        self.battery_capacity = battery_capacity

    def use(self, hours: float) -> str:
        """
        Использование смартфона. Потребление заряда на основе времени использования.

        :param hours: Количество часов использования
        :return: Строка с результатом использования
        """
        if hours < 0:
            raise ValueError("Время использования не может быть отрицательным")
        battery_consumed = hours * 10  # предположим, что смартфон тратит 10% заряда за 1 час использования
        if battery_consumed > self.battery_level:
            raise ValueError("Недостаточно заряда для использования смартфона")

        self.battery_level -= battery_consumed
        return f"Использование смартфона в течение {hours} часов. Осталось {self.battery_level}% заряда."

    def charge(self, amount: float) -> None:
        """
        Зарядка смартфона.

        :param amount: Количество заряда для подзарядки
        :raise ValueError: Если количество заряда больше, чем максимальная ёмкость батареи или меньше 0
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Количество заряда должно быть положительным числом")
        if self.battery_level + amount > self.battery_capacity:
            raise ValueError(f"Зарядка не может превысить ёмкость батареи ({self.battery_capacity}%)")
        self.battery_level += amount
        print(f"Вы подзарядили смартфон на {amount}%. Текущий уровень заряда: {self.battery_level}%.")


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

    # Пример работы класса
    phone = Smartphone("iPhone 12", 50, 100)
    print("Модель телефона: ", phone.model)
    print("Уровень зарядки", phone.battery_level)
    print("Емкость батареи", phone.battery_capacity)
    # Использование смартфона в течение 2 часов
    print(phone.use(2))
    # Зарядка на 30 процентов
    phone.charge(30)
    print("")


class SmartLamp:
    def __init__(self, brightness: float, color: str):
        """
        Инициализация умной лампы с яркостью и цветом.

        :param brightness: Яркость лампы (от 0 до 100)
        :param color: Цвет лампы
        >>> lamp = SmartLamp(75, "red")
        """
        if not isinstance(brightness, (int, float)) or not (0 <= brightness <= 100):
            raise ValueError("Яркость должна быть числом от 0 до 100")
        if not isinstance(color, str) or not color:
            raise ValueError("Цвет не может быть пустым")

        self.brightness = brightness
        self.color = color

    def turn_off(self) -> None:
        """
        Выключение лампы (устанавливается яркость в 0).
        """
        self.brightness = 0
        self.color = "off"
        print("Лампа выключена")

    def adjust_brightness_by_time(self, hour: int) -> None:
        """
        Регулирует яркость лампы в зависимости от времени суток.

        :param hour: Время в часах (24-часовой формат)
        """
        if hour < 0 or hour >= 24:
            raise ValueError("Час должен быть в пределах от 0 до 23")

        if 6 <= hour < 18:  # Днём яркость больше
            self.brightness = 100
        else:  # Ночью яркость меньше
            self.brightness = 30
        print(f"Яркость лампы установлена на {self.brightness} в зависимости от времени: {hour}:00.")


if __name__ == "__main__":
    doctest.testmod()
    lamp = SmartLamp(75, "red")
    print("Яркость лампы: ", lamp.brightness)  # 75
    print("Цвет лампы: ", lamp.color)  # 'red'

    # Регулируем яркость в зависимости от времени суток
    lamp.adjust_brightness_by_time(8)  # Утро, яркость должна быть 100
    print("Яркость лампы: ", lamp.brightness)  # 100

    lamp.adjust_brightness_by_time(20)  # Ночь, яркость должна быть 30
    print("Яркость лампы: ", lamp.brightness)  # 30

    # Выключение лампы
    lamp.turn_off()
    print("Яркость", lamp.brightness)
    print("Цвет", lamp.color)
