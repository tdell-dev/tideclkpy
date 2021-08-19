import os
import time
from threading import * 

class HDMIDispHandler():
    def __init__(self, log):
        self.log = log
        self._stop = False
        self._thread = Thread(target=self.update)

    def start(self):
        self.log.info("HDMIDispHandler started")
        self._stop = False
        self._thread.start()

    def stop(self):
        self.log.info("HDMIDispHandler stopped")
        self._stop = True
        self._thread.join()

    def update(self):
        while not self._stop:
            self.log.info("Updating Display")
            time.sleep(5)
       
        



