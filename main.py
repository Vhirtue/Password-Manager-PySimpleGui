import PySimpleGUI as sg
from database import *
import time

sg.set_options(font=("Courier", 12))

records = get_records()

#check if inputs are empty
def checkMissingInput(lst):
    for i in lst:
        if i == '':
            return True
    return False

#create window to show records
def createShowRecordsWindow():
    toprows = ["Id","Url","Username","Password"]

    showRecordsLayout = [
        [sg.Text("Records")],
        [sg.Table(key='records-table',values=records, headings=toprows, 
                  expand_x=True,
                  expand_y=True,
                  justification="center",
                  enable_click_events=True
                  ),],
        [sg.Button("Select",key="select-record",expand_x=True,enable_events=True),sg.Button("Close",key="close-show-records",expand_x=True,enable_events=True)]
    ]

    window = sg.Window("Records", showRecordsLayout, size=(800,400))
    while True:
        event, values = window.read(timeout=1000)

        #events
        if event =="close-show-records" or event == sg.WIN_CLOSED:
            break

        elif event == "select-record":
            pass
        
        window['records-table'].update(values=get_records())

#create window to add records
def main():
    addRecordsLayout = [
        [sg.Push(), sg.Text("Password Manager"), sg.Push()],

        [sg.Text("URL "), sg.Push(), sg.Input("www.apple.com",enable_events=True, key="input-url")],
        [sg.Text("Username/Email "), sg.Push(), sg.Input("johndoe@gmail.com",enable_events=True, key="input-username")],
        [sg.Text("Password "), sg.Push(), sg.Input("john123",enable_events=True, key="input-password")],

        [sg.Button("Add Record", enable_events=True, key="add-records", expand_x=True), sg.Button("Show Records", enable_events=True, key="show-records", expand_x=True), sg.Button("Clear", enable_events=True, key="clear", expand_x=True)],
    ]

    window = sg.Window("Password Manager", addRecordsLayout)

    while True:
        event, values = window.read()

        #events
        if event == sg.WIN_CLOSED:
            break
        elif event == 'clear':
            window['input-url'].update('')
            window['input-username'].update('')
            window['input-password'].update('')

        elif event == 'add-records':
            inputElementValues = list(values.values())
            try:
                if checkMissingInput(inputElementValues) == True:
                    sg.popup("Missing input values...")
                else:
                    addDbRecord(inputElementValues[0], inputElementValues[1], inputElementValues[2])
                    sg.popup("Record succesfully added...")

            except ValueError:
                print("ValueError")
        
        elif event == 'show-records':
            createShowRecordsWindow()

    window.close()

if __name__ == "__main__":
    main()