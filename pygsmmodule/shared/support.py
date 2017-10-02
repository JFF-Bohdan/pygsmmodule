import time


class SimSupportFunctions:
    @staticmethod
    def time_delta(tm_begin):
        return (time.time() - tm_begin) * 1000.0

    @staticmethod
    def parse_data(data, separator="\r", encoding="ascii"):
        if type(data) == bytearray:
            data = data.decode(encoding)

        return data.split(separator)

    @staticmethod
    def get_last_non_empty_string(data):
        for item in reversed(data):
            if len(str(item).strip()) > 0:
                return str(item).strip()

        return None

    @staticmethod
    def remove_end_result(data):
        items_qty = len(data)
        found_index = None

        for index, value in enumerate(reversed(data)):
            if str(value).strip():
                found_index = index
                break

        return data[:items_qty - (found_index + 1)] if found_index is not None else None

    @staticmethod
    def convert_to_string(values, strip=False):
        return "".join(values) if not strip else ("".join(values)).strip()
