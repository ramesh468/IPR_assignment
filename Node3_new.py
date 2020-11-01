#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import socket
import psutil

socket_conne = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ("127.0.0.1",8080)
socket_conne.connect(address) 
while True:    
            battery_use = psutil.sensors_battery()  
            message = "Battery usage: "+ str(battery_use[0])
            print(battery_use)
            socket_conne.send(message.encode())   
            time.sleep(15)
socket_conne.close()
        



