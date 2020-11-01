#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import time
import socket

socket_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ("127.0.0.1",8080)
socket_connection.connect(address) 
while True:    
            cpu_info = psutil.cpu_percent()
            print(cpu_info)
            data = {'Key':'CPU','Value': cpu_info}
            message = "CPU usage is: "+ str(data)
            socket_connection.send(str(data).encode())
            time.sleep(5)      
socket_connection.close()


