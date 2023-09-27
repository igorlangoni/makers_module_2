from time import time
from datetime import datetime, timedelta

class Time():
    def __init__(self):
        self.order_time = None
        self.delivery_time = None

    def delivery_eta(self):
        time_format = "%H:%M:%S"
        timestring = datetime.strptime(str(datetime.now() + timedelta(hours=0.5))[11:19], time_format)
        time_modification = datetime.fromtimestamp(timestring.timestamp())
        return str(timestring)[11:16]
    
    def current_time(self):
        return str(datetime.now())[11:16]
