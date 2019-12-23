#!/usr/bin/env python

import socket
import time
from data import sendDataList,host,port,Num,method




def f(n):
    try:
        addr = (host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)

        while True:
            for x in sendDataList:
                t1 = time.time()
                hex_str = x
                send_data = bytes.fromhex(hex_str)
                # print(send_data)
                s.send(send_data)
                result = s.recv(1024)
                t2 = time.time()
                recv_data = result.hex()
                with open("send_successfully.txt", '+a') as f:
                     f.write("Received_data:"+recv_data+"; usetime/send:"+format(str((t2-t1)*1000))+" ms\n")
                print("Received_data:", recv_data)
            break
        s.close()

    except Exception as e:
        with open('log.txt', 'a+') as f:
            f.write("Test failed:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")


if __name__ == '__main__':
    l = []

    for i in range(Num):
        p = method(target=f, args=[i, ])
        p.start()
        l.append(p)
    for p in l:
        p.join()