import serial


def init_serial(uart_name, uart_speed):
    return serial.Serial(
        uart_name,
        baudrate=uart_speed,
        bytesize=serial.EIGHTBITS,
        timeout=0.5,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE
    )
