#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import socket
import psutil

socket_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ("127.0.0.1",8080)
socket_connection.connect(address) 
while True:    
            memory_data = psutil.virtual_memory()
            print(memory_data[2])
            key_val = {'Key':'MEMORY','Value': memory_data[2]}
            socket_connection.send(str(key_val).encode())
            time.sleep(15)
socket_connection.close()
