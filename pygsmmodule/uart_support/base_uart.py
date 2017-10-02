import time

from pygsmmodule.shared.support import SimSupportFunctions
from pygsmmodule.shared.typesandconsts import PyGsmModuleTimeoutError, SimSpecialConsts


class BaseUart(object):
    def __init__(self, serial):
        self._serial = serial

    def _send_raw_bytes(self, data, timeout=1000):
        bytes_to_send = len(data)
        sent_bytes = 0
        start = time.time()

        while sent_bytes < bytes_to_send:
            if SimSupportFunctions.time_delta(start) >= timeout:
                raise PyGsmModuleTimeoutError

            sent_bytes += self._serial.write(data[sent_bytes:])
            if sent_bytes == 0:
                time.sleep(0.001)
                continue

        return SimSupportFunctions.time_delta(start)

    def writeln(self, data, timeout=1000):
        if type(data) == str:
            data = str(data).encode("ascii")

        data = bytearray(data) + bytearray([SimSpecialConsts.cr, SimSpecialConsts.lf])

        return self._send_raw_bytes(data, timeout)

    def send_simple_request(self, command, timeout=1000, possible_results = None):
        if type(command) == str:
            command = str(command).encode("ascii")

        if possible_results is None:
            possible_results = ["OK", "ERROR"]

        self._serial.flush()
        spent_time = self.writeln(command, timeout)
        timeout -= spent_time

        return self._read_simple_result(timeout, possible_results)

    def _read_simple_result(self, timeout, possible_results):
        tm_begin = time.time()

        read_bytes_qty = 0
        buffer = bytearray()
        while True:
            if SimSupportFunctions.time_delta(tm_begin) >= timeout:
                raise PyGsmModuleTimeoutError

            while True:
                b = self._serial.read(100)

                if (b is not None) and (len(b) >= 1):
                    buffer += bytearray(b)

                    read_bytes_qty += len(b)
                    continue
                else:
                    break

            if read_bytes_qty == 0:
                time.sleep(0.005)
                continue

            strings = SimSupportFunctions.parse_data(buffer[:])

            if len(strings) == 0:
                time.sleep(0.01)
                continue

            last_string = SimSupportFunctions.get_last_non_empty_string(strings[:])

            if last_string in possible_results:
                return SimSupportFunctions.convert_to_string(SimSupportFunctions.remove_end_result(strings))

        return None
