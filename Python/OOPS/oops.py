class SuperHero():
    def __init__(self,name,superpower):
        self.name = name
        self.superpower = superpower

    def get_superpower(self):
        print(f"I am {self.name} and My Power is {self.superpower}")    
        
batman = SuperHero("Batman","Shadow Effect")
superman = SuperHero("Super Man","Super effect")

batman.get_superpower()
superman.get_superpower()


class Sensor():
    def __init__(self,name,location,record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self,time,data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)}") 
 
    def clear_data(self):
        self.data = {}
        print("Data Cleared")

import numpy as np

sensor1 = Sensor(name="Sensor1",location="Haldia",record_date="2022-02-21")
    
print(sensor1.name,sensor1.location,sensor1.record_date)

data = np.random.randint(-10,10,10)
time = np.arange(10)
print(time)

sensor1.add_data(time=time,data=data)
print(sensor1.data)

class Accelerometer(Sensor):
    def show_type(self):
        print(f"I am {self.name}")

acc = Accelerometer(
    "accelerometer",
    "Haldia",
    "2023-01-09"
)

acc.show_type()

acc.add_data(data=data,time=time)
print(acc.data)

class Gyro(Accelerometer):
    def show_type(self):
        print(f"This is {self.name} and location is at {self.location}")

gyro = Gyro(
    name="Gyrosoope",
    location="Kolkata",
    record_date="2023-01-10"
)

gyro_data = np.random.randint(-25, 5, 10)
gyro_time = np.arange(10)

gyro.add_data(data=gyro_data, time=gyro_time)
gyro.show_type()

class GPS(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand

gps = GPS(
    name="GPS",
    location="Delhi",
    record_date="2023-01-10",
    brand="Expressif"
)

print(gps.name, gps.record_date, gps.location)
print(gps.brand)