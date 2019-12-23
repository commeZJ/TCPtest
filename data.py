#coding：utf-8
import threading
import multiprocessing
import binascii

'''
    1.用来处理和存储数据压力测试数据
'''

host = "139.224.133.113"    #ip地址
port = 59003    #端口
Num = 10 #并发数

#请求报文参数设置
head = "aa55"
CMD = [35,2]
serialNum = "0000"
app_ver = "000703285b"
IMEI = b"868183036882350"
IMSI = b"460045612201198"
fill_heart = "1c26"

#请求数据处理
hex_IMEI = binascii.b2a_hex(IMEI)  # 将字符串转换为ascii16进制的字节串
str_IMEI = bytes.decode(hex_IMEI)  # 将字节串转换为字符串
hex_IMSI = binascii.b2a_hex(IMSI)
str_IMSI = bytes.decode(hex_IMSI)
sendDataList = []
for c in CMD:
    # i = int(c)
    hex_CMD = hex(c)[2:]  #10进制数转16进制字符串（[2:]去除进制表示位"0x"）

    if c == 35:
        splice = head+hex_CMD+serialNum+hex_CMD+app_ver+str_IMEI+str_IMSI
    elif c == 2:
        hex_CMD = str(hex_CMD).zfill(2) #单个字符前面补“0”
        splice = head + hex_CMD + serialNum + hex_CMD + fill_heart
    else:
        print("不识别的指令:"+str(c)+"; 请检查你的指令类型！")
    print(splice)
    sendDataList.append(splice)
    sendDataList[0]

# sendDataList = [
#     "aa5523a400230001801500383632383638303437313531333432343630303430303739363134333731",
#     "aa5502a700020825"
#     ]

'''
multiprocessing.Process---多进程实现
threading.Thread---多线程实现
'''
# method = multiprocessing.Process
method = threading.Thread



