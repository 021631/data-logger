from main.dataset import Dataset
from sensorlib.temp import Temp
from main.logging_activity import Log
from config.config import Config
from api_plugin.sams_science import SamsApi
from numpy import median
import time


class DS18B20:
    def __init__(self):
        self.log = Log()
        self.config = Config()
        self.api = SamsApi()
        self.ds_temp = []
        self.dataset = []
        self.config_data = self.config.get_config_data()
        self.median_interval = int(self.config_data['INTERVAL']['median'])
        self.median_ds_temp = ""
        self.wait_time = int(self.config_data['INTERVAL']['wait_time_seconds'])
        try:
            self.temp = Temp()
        except Exception as e:
            self.log.write_log("Failed to initialize DS18B20: {}".format(e))

    def get_ds18b20_data(self):
        sensor_counter = self.temp.device_count()
        try:
            if sensor_counter != 0:
                for x in range(sensor_counter):
                    self.median_ds_temp = []
                    for i in range(self.median_interval):
                        value = self.temp.tempC(x)
                        if value == 998 or value == 85.0:
                            self.log.write_log("DS18B20 does not work properly...")
                        else:
                            self.ds_temp.append(self.temp.tempC(x))
                            time.sleep(self.wait_time)

                    if len(self.ds_temp) != 0:
                        self.median_ds_temp = median(self.ds_temp)
                        return({
                            "sourceId": "dsb18b20-{0}-{1}".format(x, self.api.client_id),
                            "values": [
                                {
                                    "ts": Dataset.get_time(),
                                    "value": float(self.median_ds_temp)
                                },
                            ]
                        })

        except Exception:
            return False
