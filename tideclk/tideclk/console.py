from . import requester
from . import display

def main():
    try:
        display.init()
        display.run()
    except KeyboardInterrupt:
        print("Exiting")
#    except:
#        print("Exiting due to Exception")

