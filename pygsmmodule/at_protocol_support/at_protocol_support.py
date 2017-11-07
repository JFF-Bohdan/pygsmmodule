from pygsmmodule.uart_support.base_uart import BaseUart


class AtProtocolSupport(BaseUart):
    def __init__(self, serial):
        super().__init__(serial)

    def initialize_port(self):
        commands_to_execute = [
            "ATE0"
        ]
        for command in commands_to_execute:
            res = self.send_simple_request(command, remove_result=False)

            res = res.split("\n")
            if "OK" not in res:
                return False

        return True
