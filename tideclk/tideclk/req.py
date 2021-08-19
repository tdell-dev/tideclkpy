import os
import time
import requests

from threading import Thread

class NOAARequestHandler:
    token_fn = "/etc/NCDC_auth"
    base_uri = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"
    station_id = "9414290"
    req_headers = {'token':None}

    def __init__(self, log):
        self.log = log
        self.log.info("Initilizing NOAARequestHandler")
        self.get_token()
        self.req_headers['token'] = self.token_plaintext 
        self._stop = False
        self._thread = Thread(target=self.loop_req)

    def start(self):
        self.log.info("NOAARequestHandler is starting")
        self._stop = False
        self.init_req()
        self._thread.start()

    def loop_req(self):
        while not self._stop:
            self.log.info("NOAA Request sent")
            request_string = self.compose_req()
            req = requests.get(request_string, headers=self.req_headers)
            self.log.info("NOAA Response Status: {}".format(req.status_code))
            time.sleep(1)

    def stop(self):
        self.log.info("NOAARequestHandler has been stopped")
        self._stop = True
        self._thread.join()

    def get_token(self):
        statinfo = os.stat(self.token_fn)
        if not os.path.exists(self.token_fn):
            raise RuntimeError("Failed to find token in /etc/NCDC_auth , please visit https://www.ncdc.noaa.gov/cdo-web/token and input email address to get a token")

        with open(self.token_fn, "r") as r:
            self.token_plaintext = r.readline().rstrip()
        self.log.info("Token is read as: {}".format(self.token_plaintext))


    def compose_req(self):
        return self.base_uri + "stations"


    def init_req(self):
        time.sleep(3)
        #self.log.info("Initializing Queue with 2880 samples. This is the last 24 hours and the next 24 hours")
#        for sample_index in range(2880):
        request_string = self.compose_req()
        self.log.info("request string: {}".format(request_string))
        #resp = requests.get(request_string, headers=self.req_headers)
        #self.log.info("NOAA Response Status: {}".format(resp.status_code))
        #self.log.info("NOAA Response Text: {}".format(str(resp.text)))
        #self.log.info("NOAA Response Content: {}".format(str(resp.content)))
        #self.log.info("NOAA Response Dict: {}".format(resp.__dict__))
