class Toyota:

    def __init__(self):
        self.color = "Бордовый металлик"
        self.price = "1 000 000 руб."
        self.max_velocity = "200 км/ч"
        self.current_velocity = "0 км/ч"
        self.engine_rpm = 0

    def start(self):
        print("Мотор запущен")
        self.engine_rpm = 900

    def go(self):
        print("Поехали")
        self.engine_rpm = 2000
        self.current_velocity = "20 км/ч"


my_car = Toyota()
print("color", my_car.color)
print("price", my_car.price)
print("max_velocity", my_car.max_velocity)
print("rpm", my_car.engine_rpm)
print("current_velocity", my_car.current_velocity)

my_car.start()
print("engine_rpm", my_car.engine_rpm)
my_car.go()
print("engine_rpm", my_car.engine_rpm)
print("current_velocity", my_car.current_velocity)

produced, plan = 0, 10000
stock = []
while produced < plan:
    new_car = Toyota()
    stock.append(new_car)
    produced += 1

class Robot:

    def __init__(self):
        self.name = "R2D2"

    def hello(self):
        print(f"Привет, мир - я {self.name}")


robot = Robot()
robot.hello()
