class SimSpecialConsts:
    ctrl_z = 26    # ascii character for ctr+z. End of a SMS.
    cr = 0x0d  # ascii character for carriage return.
    lf = 0x0a  # ascii character for line feed.


class Error(Exception):
    pass


class PyGsmModuleTimeoutError(Error):
    pass
