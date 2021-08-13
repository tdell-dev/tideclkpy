import requests
import os

class Requester:
    token_fn = "/etc/NCDC_auth"
    base_uri = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"
    req_headers = {'token':None}

    def __init__(self, log):
        self.log = log
        self.log.info("Initilizing Requester")
        self.get_token()
        self.req_headers['token'] = self.token_plaintext 
        self.startup_test_result = self.init_req()

    def get_token(self):
        statinfo = os.stat(self.token_fn)
        if not os.path.exists(self.token_fn):
            raise RuntimeError("Failed to find token in /etc/NCDC_auth , please visit https://www.ncdc.noaa.gov/cdo-web/token and input email address to get a token")

        with open(self.token_fn, "r") as r:
            self.token_plaintext = r.readline().rstrip()
        self.log.info("Token is read as: {}".format(self.token_plaintext))

    def init_req(self):
        r = requests.get(self.base_uri + "stations", headers=self.req_headers)
        self.log.info(r.status_code)
        self.log.info(r)


