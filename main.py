import hid
import sys
import argparse

settings = {
    # Vendor Defined
    'temp': 1,
    'saturation': 18,
    'hue': 19,
    'pic-by-pic': 32,
    'lock-osd': 33,
    'disable-osd': 34,
    'input': 35,
    'screen': 50,
    'osd-rotation': 55,
    'debug': 59,

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
parser.add_argument("setting", help="The setting number.", choices=settings, metavar='setting')
parser.add_argument("-s", "--set", help="Value to set.", type=int)

args = parser.parse_args()

dev = hid.Device(0x056d, 0x40ff)
setting = settings.get(args.setting)

if args.set is not None:
    data = setting.to_bytes(1, 'little', signed=False) + args.set.to_bytes(32, 'little', signed=False)
    res = dev.send_feature_report(data)
    print(res, 'bytes written')

else:
    data = dev.get_feature_report(setting, 33)
    num = int.from_bytes(data[0:1], 'little', signed=False)
    value = int.from_bytes(data[1:3], 'little', signed=False)

    print(value)
