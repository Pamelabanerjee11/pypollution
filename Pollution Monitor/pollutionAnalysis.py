#Do not run in ROM

import pypollution as plot
import serial.tools.list_ports as ports
import os

print("Available ports : \nPort\t Hardwere")
for i in range(len(ports.comports())):
	print(ports.comports()[i])

inputPort = input("\nEnter Ardiuno Port number : ")
try:
    p = plot.pyAnalysis(inputPort, os.path.dirname(__file__))
    p.genrateLineAnalysis()
except:
    print("An error is occurred while plotting the graph. Probable reason may be :")
    print("1. You are running app in read only memory.")
    print("2. Check your hardware port(COM port).")
    print("3. Wrong port assignment.")