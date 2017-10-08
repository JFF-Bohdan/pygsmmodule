# pygsmmodule

![](https://travis-ci.org/JFF-Bohdan/pygsmmodule.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/JFF-Bohdan/pygsmmodule/badge.svg?branch=master)](https://coveralls.io/github/JFF-Bohdan/pygsmmodule?branch=master)

*GSM modem control library for SIM-800/SIM-900 modules.*

## Overview

Library able to control GSM modems SIM800/SIM900 connected via serial interface.


## Install

### Automatic installation from PyPi

You can automatically install pygsmmodule from PyPi just by typing:

`pip install pygsmmodule`


### Manual installation

In case if you want install from archive you can download latest version from [PyPi](https://pypi.python.org/pypi/pygsmmodule) after you download and extract, you can install `pygsmmodule` just by typing

`python setup.py install`

This method also can be used for source files cloned from [github](http://github.com/JFF-Bohdan/pygsmmodule) repository.

Warning! You also need install dependancies listed in `requirements.txt`


## Usage

You can find usage examples in `examples` folder. This folder also contains [README.md](./examples/README.md) file with detailed description of each example.

## Testing

First of all you need install all development dependancies listed in `requirements-dev.txt`. Next you can run tests by executing:

`python -m pytest tests -vv`

You can run tests with coverage information collecting by

`python -m pytest tests -vv --cov=pygsmmodule`
