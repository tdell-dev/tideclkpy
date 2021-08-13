import time
import logging
from systemd.journal import JournaldLogHandler

#internal classes
from . import requester
from . import display

#set up logging
logger = logging.getLogger(__name__)
journald_handler=JournaldLogHandler()
journald_handler.setFormatter(logging.Formatter(
    '[%(levelname)s] %(message)s'
))
logger.addHandler(journald_handler)
logger.setLevel(logging.DEBUG)

def main():
    logger.info('TideClk Started!')
    retry=0
    while retry ==0:
        logger.info('Attempting request')
        try:
            display.init()
            req = requester.Requester(log=logger)
            display.run()
            retry =0
  
        except KeyboardInterrupt:
            logger.info("Exiting due to Keyboard Interrupt")
        except:
            logger.info("Retrying due to Exception")
            time.sleep(1)
            retry = 1
