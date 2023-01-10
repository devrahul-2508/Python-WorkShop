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