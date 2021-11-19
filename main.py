#! /usr/bin/python

import hid
import argparse

settings = {
    # Vendor Defined
    'temp': 1,
    'identify': 2,
    'profile': 3,
    'saturation': 18,
    'hue': 19,
    'power': 20,
    'horizontal-res': 25,
    'vertical-res': 26,
    'sensor': 30,
    'button': 31,
    'pic-by-pic': 32,
    'lock-osd': 33,
    'disable-osd': 34,
    'input': 35,
    'eco-settings2' : 44,
    'screen': 50,
    'osd-rotation': 55,
    'debug': 59,
    'factory-lum' : 71,
    'gain-def': 76,

    # Consumer
    'volume': 81,

    # VESA
    'brightness': 82,
    'contrast': 83,
    'red': 84,
    'green': 85,
    'blue': 86,
}

parser = argparse.ArgumentParser()
parser.add_argument("setting", help="The setting number.")
parser.add_argument("-s", "--set", help="Value to set.", type=int)
parser.add_argument("-i", "--id", help="Use setting id.", action='store_true')

args = parser.parse_args()

if args.id is True:
    setting = int(args.setting)
else:
    setting = settings.get(args.setting)

dev = hid.Device(0x056d, 0x40ff)

if args.set is not None:
    data = setting.to_bytes(1, 'little', signed=False) + args.set.to_bytes(32, 'little', signed=False)
    res = dev.send_feature_report(data)
    print(res, 'bytes written')

else:
    data = dev.get_feature_report(setting, 200)
    num = int.from_bytes(data[0:1], 'little', signed=False)
    value = int.from_bytes(data[1:3], 'little', signed=False)

    if setting == 44:
        bpb = int.from_bytes(data[1:2], 'little', signed=False)
        bpa = int.from_bytes(data[2:4], 'little', signed=False)
        dpb = int.from_bytes(data[4:5], 'little', signed=False)
        dpa = int.from_bytes(data[5:7], 'little', signed=False)
        inf = int.from_bytes(data[7:9], 'little', signed=False)

        print("Bright Point Brightness:        ", bpb)
        print("Bright Point Ambient Light:     ", bpa)
        print("Dark Point Brightness:          ", dpb)
        print("Dark Point Ambient Light:       ", dpa)
        print("Inflection Point Ambient Light: ", inf)

    elif setting == 71:
        r = int.from_bytes(data[1:3], 'little', signed=False)
        g = int.from_bytes(data[3:5], 'little', signed=False)
        b = int.from_bytes(data[5:7], 'little', signed=False)
        w = int.from_bytes(data[7:9], 'little', signed=False)

        print("Red:   ", r / 10)
        print("Green: ", g / 10)
        print("Blue:  ", b / 10)
        print("White: ", w / 10)

    elif setting == 76:
        print("Gain Definition")

        for i in range(0, 25):
            pos = 6 * i
            r = int.from_bytes(data[((i * 6) + 0):((i * 6) + 1)], 'little', signed=False)
            g = int.from_bytes(data[((i * 6) + 1):((i * 6) + 2)], 'little', signed=False)
            b = int.from_bytes(data[((i * 6) + 2):((i * 6) + 3)], 'little', signed=False)

            print(r, g, b)

    else:
        print(value)
        print(data.hex())

