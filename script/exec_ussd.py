from pygsmmodule.at_protocol_support.at_protocol_support import AtProtocolSupport
from pygsmmodule.supplementary.ussd_executor import UssdExecutor

from .shared import init_serial, load_dev_config


def main(**kwargs):
    settings = load_dev_config()
    serial = init_serial(settings.uart.name, settings.uart.speed)
    at_executor = AtProtocolSupport(serial)

    print("initializing port...")
    ok = at_executor.initialize_port()

    if ok:
        print("initialization [  OK  ]")
    else:
        print("initialization [FAILED]")
        return 1

    ussd_command = "*101#"
    result = UssdExecutor.exec_command(at_executor, ussd_command)

    result = str(result).strip()
    print("executing USSD command '{}' result:\n---\n{}\n---".format(ussd_command, result))

    serial.close()


if __name__ == "__main__":
    res = main()
    exit(res)
