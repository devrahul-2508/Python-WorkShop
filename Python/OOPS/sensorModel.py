class Sensor():
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self._record_date = "2023-01-10"
        self.__version = "0.1"
        self.data = {}

    def getRecoudDate(self):
        print("The record date = ", self._record_date)

    def getVersion(self):
        print("The version = ", self.__version)

    def setVersion(self, version):
        self.__version = version
        print(f"New version {self.__version}")

    def setRecordDate(self, recordDate):
        self._record_date = recordDate
        print("New record date = ", self._record_date)

    def add_data(self,time,data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)}") 
 
    def clear_data(self):
        self.data = {}
        print("Data Cleared")

sensor = Sensor(
    name="Sensor1",
    location="Haldia"
)

print(sensor.name)
sensor.getRecoudDate()
sensor.getVersion()
sensor.setVersion("0.2")
sensor.setRecordDate("2023-01-11")
sensor.getRecoudDate()
sensor.getVersion()