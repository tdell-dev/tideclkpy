import os
import time
import logging
import time
import tkinter as tk

from threading import *
from systemd.journal import JournaldLogHandler

#internal classes
from .req import NOAARequestHandler
from .disp import HDMIDispHandler

#set up logging
logger = logging.getLogger(__name__)

journald_handler=JournaldLogHandler()
journald_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))

file_handler=logging.FileHandler('/home/pi/.tideclk_log.log')
file_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))

logger.addHandler(journald_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def init_disp(tk_root):
    if os.environ.get('DISPLAY', '') == '':
        print('WARNING: No display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
    tk_root.attributes("-fullscreen", True)
    tk_root.wm_attributes("-topmost", True)
    tk_root['bg'] = "#000000"

def main():
    #At a high level, the goal is as follows:
    #    Create a Requester Object
    #    Create a Display Object
    #    Within thread, kick off func that pings NOAA data every second
    #    Within thread, kick off func that updates Display data every time new NOAA data arrives ( status 200 )
    #    Continually update tkinter render until Keyboard interrupt is received

    root = tk.Tk()
    init_disp(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    logger.info("Screen Width: {}".format(screen_width))
    logger.info("Screen Height: {}".format(screen_height))
    
    disp = HDMIDispHandler(logger)
    disp.start()

    req = NOAARequestHandler(logger)
    req.start()

    logger.info('TideClk Started!')

    canvas = tk.Canvas(root)
    canvas.pack(fill='both', expand=True)
    canvas.create_oval((0,0, screen_width, screen_height), fill='red', outline='black')

    root.mainloop()

    time.sleep(50)

    disp.stop()
    req.stop()
    
    #retry=1
    #while retry:
    #    logger.info('Attempting request')
    #    try:
    #        display.init()
    #        req = requester.Requester(log=logger)
    #        display.run()
    #        retry =0
 #
 ####   except KeyboardInterrupt:
 ####       logger.info("Exiting due to Keyboard Interrupt")
 ####       loop.stop()
 ####       loop.close()
 ####   except:
 ####       logger.info("Retrying due to Exception")
 ####       time.sleep(1)
 ####       retry = 1

def on_escape(event=None, root=None):
    print("escaped")
    root.destroy()
