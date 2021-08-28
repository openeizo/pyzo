# pyzo

This is a small python script to control Eizo monitors using the the [linux driver](https://github.com.com/openeizo/openeizo).

----
## Example
To read the brightness value:
```
$ python main.py brightness
160
```
To set the brightness value:
```
$ python main.py brightness -s 170
```
----
To switch inputs:

HDMI
```
$ python main.py input -s 1024
```

DVI
```c
$ python main.py input -s 512
```

PicbyPic DP1 & DP2
```
$ python main.py pic-by-pic -s 1
$ python main.py screen -s 0
$ python main.py input -s 768
$ python main.py screen -s 1
$ python main.py input -s 769
```
