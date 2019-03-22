import datetime
from credentials import Credentials
from api_plugin.ondo import OndoApi


# for debug purpose
class Log:
    def __init__(self):
        self.name = "log"
        self.api = OndoApi()

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%dT%H:%M:%S') + now.strftime('.%f')[:0] + 'Z'

    def write_log(self, message):
        try:
            file = open(Credentials.activity_path, "a+")
            file.write("{}\n{}\n".format(message, self.get_time()))
            file.close()
        except:
            pass

        try:
            self.api.post_activity(message)
        except:
            pass
