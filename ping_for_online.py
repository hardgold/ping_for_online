import os
import time

#ip_list
ip_list = ['www.baidu.com','www.sina.com','www.sina.com.cn','www.taobao.com','www.qidian.com']

while (ip_list != None):
    for ip in ip_list:
        try:
            print('ping start:',ip)
            os.system('ping -c 2 {0}'.format(ip))
            time.sleep(301)
            print('='*60)
        except:
            ip_list.pop(ip)


