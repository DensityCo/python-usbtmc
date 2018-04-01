## Introduction

Python USBTMC provides a pure Python USBTMC driver for controlling instruments
over USB.

## Installation
```bash
sudo pip install --upgrade pip
sudo pip install pyusb
sudo python setup.py install
```

## Configuring udev
```bash
sudo cp usbtmc.rules /etc/udev/rules.d
sudo udevadm control --reload-rules && udevadm trigger
```

## Usage
```bash
python 9202.py
```
