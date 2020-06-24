#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: demo.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 6月 12, 2020
# ---

from time import sleep

import serial

import serial.tools.list_ports


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(r'/x')[1:]]])


def portlist():
    plist = list(serial.tools.list_ports.comports())

    if len(plist) <= 0:
        print("The Serial port can't find!")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName, 9600, timeout=60)
        print("check which port was really used >", serialFd.name)
        return serialFd.name


def readport():
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = "COM6"

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = 115200

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = None

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)
        print("串口详情参数：", ser)

        # # 十六进制的发送
        # result = ser.write(chr(0x06).encode("utf-8")) # 写数据
        # print("写总字节数：", result)

        # 十六进制的读取
        print(ser.read().hex())  # 读一个字节

        print("----------")
        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


def portwrite(port, bps):
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = port

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = bps

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = 5

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)

        # 写数据
        result = ser.write("HELLO WORLD".encode("gbk"))
        print("写总字节数：", result)

        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


def portwrite16(port, bps, arg):
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = port

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = bps

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = 10

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)

        # 写数据
        result = ser.write(arg)
        print("写总字节数：", result)
        if ser.read(6).hex() == '3a0602030106':
            print("Successful")
        else:
            print("Failed")

        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


def portpower16(port, bps, arg):
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = port

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = bps

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = 10

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)

        # 写数据
        result = ser.write(arg)
        print("写总字节数：", result)
        # print(ser.read(6).hex())
        if ser.read(6).hex() == '3a0602040107':
            print("Successful")
        else:
            print("Failed")

        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


if __name__ == "__main__":
    port = portlist()  # 获取串口号
    bps = 115200  # 设定波特率
    usb_power_on = [0x3C, 0x08, 0x01, 0x03, 0x02, 0x01, 0x02, 0x09]
    connect_pc = [0x3C, 0x07, 0x01, 0x03, 0x03, 0x12, 0x19]
    connect_B_1 = [0x3C, 0x07, 0x01, 0x03, 0x01, 0x12, 0x17]
    connect_B_2 = [0x3C, 0x07, 0x01, 0x03, 0x03, 0x11, 0x18]
    usb_switch_check = [0x3A, 0x06, 0x02, 0x03, 0x01, 0x06]  # 3a0602030106
    power_on = [0x3C, 0x08, 0x01, 0x04, 0x03, 0x01, 0x01, 0x0A]
    power_off = [0x3C, 0x08, 0x01, 0x04, 0x03, 0x01, 0x00, 0x09]
    power_check = [0x3A, 0x06, 0x02, 0x04, 0x01, 0x07]  # 3a0602040107

    # portwrite16(port, bps, arg=usb_power_on)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_pc)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_B_1)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_B_2)
    # sleep(5)
    portpower16(port, bps, arg=power_on)
    # sleep(5)
    # portpower16(port, bps, arg=power_off)
