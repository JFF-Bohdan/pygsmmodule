# Examples for pygsmmodule

This folder contains usage examples for [pygsmmodule](http://github.com/JFF-Bohdan/pygsmmodule) library.


## General information

Examples can contain variables `PORT` and `BAUDRATE` which specifies UART name and connection baudrate. First of all you need found valid settings for your connection.

For example, **on my machine** under Windows OS control with SIM900 module connected via [FOCA](https://www.itead.cc/foca.html) (UART to USB convertor) valid settings will be

```Python
PORT = "com22"
BAUDRATE = 57600
```


Examples list:

* `retrieve_imei.py` - retrieves IMEI from GSM module.

## Retrieve IMEI `retrieve_imei.py`

Example can be found in `examples/retrieve_imei.py`.

Can be executed by  `python .\examples\retrieve_imei.py` returns IMEI for connected GSM module.
