class Sensor():
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.__record_date = "2023-01-10"
        self.__version = "0.001"
        self.data = {}

    def add_data(self,time,data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)}") 
 
    def clear_data(self):
        self.data = {}
        print("Data Cleared")

    def get_record_date(self):
        print(f"The record date for {self.name} is {self.__record_date}")    

    def get_version(self):
        print(f"The version for {self.name} is {self.__version}") 

    def set_version(self,version):
        self.__version = version
        print(f"The version for {self.name} is {self.__version}") 

   


sensor = Sensor(
    name="Sensor1",
    location="Kolkata"
)

print(sensor.name)
sensor.get_record_date()
sensor.get_version()
sensor.set_version("5")
sensor.get_version()

