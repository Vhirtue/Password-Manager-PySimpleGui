import PySimpleGUI as sg
from database import *

sg.set_options(font=("Courier", 12))

#get all added records from database
records = getRecords()
print(records)

#check if inputs are empty
def checkMissingInput(lst):
    for i in lst:
        if i == '':
            return True
    return False

#create window to add records
def main():
    #root/main layout
    addRecordsLayout = [
        [sg.Push(), sg.Text("Password Manager"), sg.Push()],
        [sg.Text("URL "), sg.Push(), sg.Input("www.apple.com",enable_events=True, key="input-url")],
        [sg.Text("Username/Email "), sg.Push(), sg.Input("johndoe@gmail.com",enable_events=True, key="input-username")],
        [sg.Text("Password "), sg.Push(), sg.Input("john123",enable_events=True, key="input-password")],

        [sg.Button("Add Record", enable_events=True, key="add-records", expand_x=True), 
         sg.Button("Show Records", enable_events=True, key="show-records", expand_x=True), 
         sg.Button("Clear", enable_events=True, key="clear", expand_x=True)]
    ]

    #second layout, for viewing table of records
    toprows = ["Id","Url","Username","Password"]
    showRecordsLayout = [
        [sg.Push(),sg.Text("Records"),sg.Push()],
        [sg.Push(),sg.Table(key='records-table',values=records, headings=toprows, 
                  expand_x=True,
                  expand_y=True,
                  justification="center",
                  auto_size_columns=True,
                  enable_click_events=True 
                  ),sg.Push()],
        [sg.Button("Select",key="select-records",expand_x=True,enable_events=True),
         sg.Button("Exit",key="exit-show-records",expand_x=True,enable_events=True)]
    ]

    #third layout, for viewing selected layout from table
    showSelectedRecordLayout = [
        #[sg.Text(f"Record {selectRecordId}")]
        [sg.Text("Url: ")],
        [sg.Text("Username: ")],
        [sg.Text("Password: ")],

        [sg.Button("Delete", expand_x=True, key="delete-record-button"),
         sg.Button("Return", expand_x=True, key="exit-selected-record")]
    ]

    rootLayout = [[sg.Column(addRecordsLayout, key="column-1", visible=True)],
                  [sg.Column(showRecordsLayout, key="column-2", visible=False)],
                  [sg.Column(showSelectedRecordLayout, key="column-3", visible=False)]]

    window = sg.Window("Password Manager", rootLayout)
    while True:
        event, values = window.read()
    
        #events
        if event == sg.WIN_CLOSED:
            print(event)
        
            break
        elif event == 'clear':
            window['input-url'].update('')
            window['input-username'].update('')
            window['input-password'].update('')

        elif event == 'add-records':
            inputElementValues = list(values.values()) #get list all values in input elements
            try:
                if checkMissingInput(inputElementValues) == True:
                    sg.popup("Missing input values...")
                else:
                    addDbRecord(inputElementValues[0], inputElementValues[1], inputElementValues[2]) #add list of input values to database table
                    sg.popup("Record succesfully added...")

            except ValueError:
                print("ValueError")
        
        elif event == 'show-records':
            window["column-1"].update(visible=False)
            window["column-2"].update(visible=True)
            window['records-table'].update(values=getRecords()) #update records table to display new added records based on whats in database table

        if event == 'exit-show-records':
            window["column-1"].update(visible=True)
            window["column-2"].update(visible=False)

        elif event == 'select-records':
            window["column-2"].update(visible=False)
            window["column-3"].update(visible=True)
            print(values['records-table'])
        
        elif event == 'exit-selected-record':
            window["column-2"].update(visible=True)
            window["column-3"].update(visible=False)
    window.close()

if __name__ == "__main__":
    main()