import wmi
import platform

S = wmi.WMI()
my_system = S.Win32_ComputerSystem()[0]
OpSys = platform.system()

ch = input("Press zero 0 to see the features of your computer: ")

while True:
    if ch == '0':
      print("\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
      print(f"\tManufactured: {my_system.Manufacturer}")
      print(f"\tModell: {my_system.Model}")
      print(f"\tName: {my_system.Name}")
      print(f"\tOperator System: {OpSys}")
      print(f"\tSystem Type: {my_system.SystemType}")
      print(f"\tSystem Family / Computer Type: {my_system.SystemFamily}")
      print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
      break
    else:
      ch = input("ERROR, Press zero 0 to see the features of your computer: ")

print('Thanks for using this program')