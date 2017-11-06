class UssdExecutor(object):
    def __init__(self):
        pass

    @staticmethod
    def exec_command(at_executor, command, timeout=1000, read_timeout=20000):
        cmd = "AT+CUSD=1,\"{0}\",15".format(command)

        res = at_executor.send_simple_request(cmd, timeout, remove_result=False)
        if not res:
            return None

        res = str(res).strip()

        if res != "OK":
            return None

        ntr = at_executor.read_pattern_terminated_string(read_timeout)

        ntr = str(ntr).strip()

        ntr = UssdExecutor._remove_prefix(ntr, "+CUSD:")

        return UssdExecutor._remove_quotes(ntr)

    @staticmethod
    def _remove_prefix(value, prefix):
        if not str(value).startswith(prefix):
            return value

        return value[len(prefix):]

    @staticmethod
    def _remove_quotes(value):
        lindex = str(value).index("\"")
        rindex = str(value).rindex("\"")

        if (lindex == rindex) or (-1 in [lindex, rindex]):
            return value

        return value[lindex + 1: rindex]
