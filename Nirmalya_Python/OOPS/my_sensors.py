from sensorModel import Sensor

class Accelerometer(Sensor):
    def show_type(self):
        print(f"I am {self.name}")

class Gyro(Accelerometer):
    def show_type(self):
        print(f"This is {self.name} and location is at {self.location}")

class GPS(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand