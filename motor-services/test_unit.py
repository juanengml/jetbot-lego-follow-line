from motor import Arduino
from time import sleep
from lodge import logger 
arduino = Arduino()


def test_unit_motor():
    arduino.controle(b"w")
    sleep(5)

    arduino.controle(b"s")
    sleep(5)

    arduino.controle(b"a")
    sleep(5)

    arduino.controle(b"d")
    sleep(5)

    arduino.controle(b"p")


if __name__ == "__main__":
    logger.info("Test Unit...")
    test_unit_motor()
