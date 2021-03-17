import PySimpleGUI as sg

sg.theme('DarkAmber') # theme of the window

import wmi  #windows menagement system library
import platform

# Take information abuot your operating system
OpSys = platform.system()

S = wmi.WMI()
my_system = S.Win32_ComputerSystem()[0]

password = '1012'
# Define the window's contents
layout = [[sg.Text("Get your computer's information, put in your password: ")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')],
          [sg.Text(size=(300,1), key='-OUTPUT-')]
         ]

# Create the window
window = sg.Window('Get Pc Info', layout, size=(800, 400))

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # If password is correct the window give you your information
    elif values['-INPUT-'] == password:
        window['-OUTPUT-'].update('Your info: Deca')

        # pop up your computer information, in a new window
        sg.popup(
                 f"\nManufactured: {my_system.Manufacturer}",
                 f"\nModell: {my_system.Model}",
                 f"\nName: {my_system.Name}",
                 f"\nOperator System: {OpSys}",
                 f"\nSystem Type: {my_system.SystemType}",
                 f"\nSystem Family / Computer Type: {my_system.SystemFamily}"
               )
    # If you put wrong password
    elif values['-INPUT-'] != password:
        window['-OUTPUT-'].update('Error: unexpected password, try again!')

# Finish up, it remove window rom the screen
window.close()
