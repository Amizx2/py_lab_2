from task_1 import Car, Smartphone, SmartLamp

if __name__ == "__main__":
    car = Car("Nissan silvia s15", 2000, 50, 65)
    phone = Smartphone("iPhone 12", 50, 100)
    lamp = SmartLamp(75, "red")

    try:
        car.drive(-100)
    except ValueError as e:
        print('Ошибка: неправильные данные')
    try:
        car.refuel(-10)
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        phone.use(-2)
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        phone.charge(-30)
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        lamp.adjust_brightness_by_time(25)
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        lamp.adjust_brightness_by_time(-1)
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        lamp.turn_off()
    except Exception as e:
        print('Ошибка: неправильные данные')
