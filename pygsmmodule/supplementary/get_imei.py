class GetImei(object):
    def __init__(self):
        pass

    @staticmethod
    def exec_command(at_executor, timeout=1000):
        res = at_executor.send_simple_request("AT+GSN", timeout)
        return str(res).strip() if res else res
