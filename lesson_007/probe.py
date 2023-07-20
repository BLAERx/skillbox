# class Toyota:
#
#     def __init__(self):
#         self.color = "Бордовый металлик"
#         self.price = "1 000 000 руб."
#         self.max_velocity = "200 км/ч"
#         self.current_velocity = "0 км/ч"
#         self.engine_rpm = 0
#
#     def start(self):
#         print("Мотор запущен")
#         self.engine_rpm = 900
#
#     def go(self):
#         print("Поехали")
#         self.engine_rpm = 2000
#         self.current_velocity = "20 км/ч"
#
#
# my_car = Toyota()
# print("color", my_car.color)
# print("price", my_car.price)
# print("max_velocity", my_car.max_velocity)
# print("rpm", my_car.engine_rpm)
# print("current_velocity", my_car.current_velocity)
#
# my_car.start()
# print("engine_rpm", my_car.engine_rpm)
# my_car.go()
# print("engine_rpm", my_car.engine_rpm)
# print("current_velocity", my_car.current_velocity)
#
# produced, plan = 0, 10000
# stock = []
# while produced < plan:
#     new_car = Toyota()
#     stock.append(new_car)
#     produced += 1
#
# class Robot:
#
#     def __init__(self):
#         self.name = "R2D2"
#
#     def hello(self):
#         print("Привет, мир!")
#
#     def go(self, x, y):
#         print("Иду в точку", x, y)
#
#
# robot = Robot()
# robot.go(x=100, y=200)
#


class Backpack:

    def __init__(self, gift = None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def inspect(self):
        print("В рюкзаке лежит:")
        for item in self.content:
            print("   ", item)


my_backpack = Backpack(gift="флешка")
my_backpack.add("ноутбук")
my_backpack.add("зарядка от ноутбука")
my_backpack.inspect()

