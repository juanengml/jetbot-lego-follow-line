from serial import Serial
from lodge import logger


class Arduino(object):
    def __init__(self):
        try:
            self.arduino = Serial("/dev/ttyUSB0", 9600)
            logger.info("Serial Port: /dev/ttyUSB0 9600")
        except Exception as error:
            logger.error(error)

    def controle(self, ctrl):
        logger.info(f"Commander {ctrl}")
        self.arduino.write(ctrl)
