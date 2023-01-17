import numpy as np
from sensorModel import Sensor
from my_sensors import Accelerometer, Gyro, GPS

#define accelerometer object
acc = Accelerometer(
    name="Accelerometer_s1",
    location="Haldia",
    record_date="2023-01-10"
)

#define gyro object
gyro = Gyro(
    name="Gyroscope_s1",
    location="Haldia",
    record_date="2023-01-10"
)

#define gps object
gps = GPS(
    name="GPS",
    location="Delhi",
    record_date="2023-01-10",
    brand="Expressif"
)

#get data
time = np.arange(10)
acc_data = np.random.randint(-20,20,10)
gyro_data = np.random.randint(-10,10,10)
gps_data = np.random.randint(-10,5,10)

# add data
acc.add_data(time, acc_data)
gyro.add_data(time, gyro_data)
gps.add_data(time, gps_data)

#print data
print("Accelerometer = ", acc.data)
print("Gyroscope = ", gyro.data)
print("Gps = ", gps.data)