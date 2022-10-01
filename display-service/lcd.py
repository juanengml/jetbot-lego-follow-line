from jtop_read import jtop_sensors
import i2c_lcd_driver
from time import sleep
from datetime import datetime as dt
from lodge import logger
from os import popen
import re

ifconfig = popen("ifconfig wlan0").read()
regex = r"(?<=inet.)(.*)(?=netmask)"

ip = re.findall(regex, ifconfig)[0].replace(" ","")
logger.info(ip)

mylcd = i2c_lcd_driver.lcd()

def show_ip_lcd():
    hora = str(dt.now()).split(".")[0]
    logger.info(f"{ip} {hora}")
    show_msg(ip, hora)
    sleep(5)


def show_msg(msg_up, msg_down=" "):
    mylcd.lcd_clear()
    mylcd.lcd_display_string(f"{msg_up}", 1)
    mylcd.lcd_display_string(f"{msg_down}", 2)


def get_sensors():
    data = jtop_sensors()
    data["time"] = str(data["time"])
    data["uptime"] = str(data["uptime"])
    msg_up = "RAM A0 GPU CUR"
    msg_down = "{}  {}  {}  {}".format(
        round(data["RAM"] / 10000),
        round(data["Temp AO"]),
        data["GPU"],
        data["power cur"] / 100,
    )
    logger.info(f"{msg_up} {msg_down}")
    show_msg(msg_up, msg_down)
    sleep(5)


def clean_lcd():
    show_msg(" ", " ")
    sleep(1)


def main():
    while 1:
        clean_lcd()
        show_ip_lcd()
        clean_lcd()
        get_sensors()


if __name__ == "__main__":
    main()
