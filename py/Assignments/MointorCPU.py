#!/bin/python3
import psutil

#monitor the health of the CPU uisnf psutil library
if __name__ == '__main__':

    while True:

        cpu_percent =psutil.cpu_percent(interval=1)

        if ( cpu_percent < 80):
            print("CPU is healthy - CPU usage is   : %s", cpu_percent)
            break
        else:
            print("Alert! CPU usage exceeds threshold: %s", cpu_percent)