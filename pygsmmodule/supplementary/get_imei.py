from pygsmmodule.uart_support.base_uart import BaseUart


class GetImei(object):
    def __init__(self):
        pass

    @staticmethod
    def get_imei(serial, timeout=1000):
        communicator = BaseUart(serial)

        res = communicator.send_simple_request("AT+GSN", timeout)
        return str(res).strip() if res else res
