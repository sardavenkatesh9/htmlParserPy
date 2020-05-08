import sys
import csv
from datetime import datetime
import os

class excel:
    _file_name = ''

    ### Initialize csv logiv
    ### File Name is based on year month date logic
    ### Create file if not exists
    def __init__(self,title = "Temperature"):
        self._file_name = os.getcwd() + "\\" + datetime.now().strftime("%Y_%m_%d") + ".csv"
        if not os.path.exists(self._file_name):
            with open(self._file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(["Time", title])
        else:
            print('Warning: File already exists')
        return None
    ### Write Data to csv
    ### Storead as Time, Temperature Value
    ### Future Modification adding City of recorded temperature
    def write_data(self,data = 0.0):
        with open(self._file_name, "a+")as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%H:%M:%S"),str(data)])
        return None

    def write_data(self,data = ''):
        with open(self._file_name, "a+")as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%H:%M:%S"),data])
        return None

            
#Testing Code for class function excel        
##x = excel()
##x.write_data(02.0)



