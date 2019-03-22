import requests
from credentials import Credentials
import configparser


class OndoApi:
    def __init__(self):
        self.path = Credentials.ondo_path
        self.config = configparser.ConfigParser()
        self.config.read(Credentials.credentials_path)
        self.secret_data = self.config['DEFAULT']
        self.client_id = self.secret_data['client_id']
        self.apikey = self.secret_data['ondo_key']

    def post_activity(self, message):
        print("{0}?id={1}&message={2}&key={3}".format(Credentials.ondo_path, self.client_id, message,
                                                      self.apikey))
        try:
            r = requests.post(
                "{0}?id={1}&message={2}&key={3}".format(Credentials.ondo_path, self.client_id, message,
                                                        self.apikey))
            print(r)
        except Exception as e:
            print("ondo failed: {}".format(e))
