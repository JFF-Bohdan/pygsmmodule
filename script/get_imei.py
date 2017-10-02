from pygsmmodule.supplementary.get_imei import GetImei

from .shared import init_serial, load_dev_config


def main(**kwargs):
    settings = load_dev_config()
    serial = init_serial(settings.uart.name, settings.uart.speed)

    imei = GetImei.get_imei(serial)
    print("imei = '{}'".format(imei))

    serial.close()


if __name__ == "__main__":
    main()
