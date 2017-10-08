from pygsmmodule.supplementary.get_imei import GetImei
from pygsmmodule.uart_support.shared import init_serial

PORT = "com22"
BAUDRATE = 57600


def main():
    serial = init_serial(PORT, BAUDRATE)

    imei = GetImei.get_imei(serial)
    print("imei = '{}'".format(imei))

    serial.close()


if __name__ == "__main__":
    main()
