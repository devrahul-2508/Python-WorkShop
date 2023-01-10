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