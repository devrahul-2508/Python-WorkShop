from sensorModule import Sensor
from mysensors import Accelerometer,Gyro,GPS
import OOPS.numpy as np

#define a accelerometer object
acc = Accelerometer(
    "accelerometer",
    "Haldia",
    "2023-01-09"
)

#define a gyro object

gyro = Gyro(
    name="Gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
    )

#define a gps object
gps = GPS(
    name="GPS",
    location="Delhi",
    record_date="2023-01-01",
    brand="Espreesif"
)

#get data
time=np.arange(10)
acc_data = np.random.randint(-20,20,10)
gyro_data = np.random.randint(-10,30,10)
gps_data = np.random.randint(-10,5,10)

# add data to sensors
acc.add_data(data=acc_data,time=time)
gyro.add_data(data=gyro_data,time=time)
gps.add_data(data=gps_data,time=time)

print("Accelerometer data",acc.data)
print("Gyro data",gyro.data)
print("GPS data",gps.data)
