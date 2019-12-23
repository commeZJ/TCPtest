#coding：utf-8
import time
'''
asdfa
'''

str_origin = input("请输入你要解析的报文：")
# str_origin = "aa5502a400045da7d574"
str1 = str_origin[-8:]
str2 = int(str1,16)
if  str2 <1000000000 or str2 >2000000000:
    print("报文中提取的时间无效，请检查！")
else:
    str3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(str2))
    print("报文中的时间为："+str3)