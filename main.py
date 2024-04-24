import PySimpleGUI as sg
from database import *

sg.set_options(font=("Courier", 12))

#get all added records from database
records = getRecords()

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
                  #expand_x=True,
                  #expand_y=True,
                  justification="center",
                  col_widths = [5, 25, 25, 25],
                  auto_size_columns=False,
                  enable_click_events=True 
                  ),sg.Push()],
        [sg.Button("Select",key="select-records",expand_x=True,enable_events=True),
         sg.Button("Return",key="exit-show-records",expand_x=True,enable_events=True)]
    ]

    #third layout, for viewing selected layout from table
    showSelectedRecordLayout = [
        [sg.Push(),sg.Text("...", key="selected-record-id"),sg.Push()],
        [sg.Text("Url: "), sg.Push(), sg.Text("...", key="selected-record-url")],
        [sg.Text("Username: "), sg.Push(), sg.Text("...", key="selected-record-username")],
        [sg.Text("Password: "), sg.Push(), sg.Text("...", key="selected-record-password")],

        [sg.Button("Delete", expand_x=True, key="delete-record-button"),
         sg.Button("Return", expand_x=True, key="exit-selected-record")]
    ]

    rootLayout = [
        [sg.Column(addRecordsLayout, key="column-1", visible=True, expand_x=True, expand_y=True),
         sg.Column(showRecordsLayout, key="column-2", visible=False, expand_x=True, expand_y=True),
         sg.Column(showSelectedRecordLayout, key="column-3", visible=False, expand_x=True, expand_y=True)],
    ]

    window = sg.Window("Password Manager", rootLayout)
    while True:
        event, values = window.read()

        #events
        if event == sg.WIN_CLOSED:
            break

        #clear all input fields
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

        #open layout of records table
        elif event == 'show-records':
            window["column-1"].update(visible=False)
            window["column-2"].update(visible=True)
            window['records-table'].update(values=getRecords()) #update records table to display new added records based on whats in database table

        #return to add records layout
        if event == 'exit-show-records':
            window["column-1"].update(visible=True)
            window["column-2"].update(visible=False)

        #open layout of selected records
        elif event == 'select-records':
            selected_row = values['records-table'][0]#Get the index of the selected row
            selected_row_data = records[selected_row]#Get the data of the selected row
            print(f"Selected Row Data: {selected_row_data}")

            window["column-2"].update(visible=False)
            window["column-3"].update(visible=True)

            #update all text elements in selected record layout to display selected row data
            window["selected-record-id"].update(f"Record Id: {selected_row_data[0]}")
            window["selected-record-url"].update(f"{selected_row_data[1]}")
            window["selected-record-username"].update(f"{selected_row_data[2]}")
            window["selected-record-password"].update(f"{selected_row_data[3]}")

        #return to records table layout
        elif event == 'exit-selected-record':
            window["column-2"].update(visible=True)
            window["column-3"].update(visible=False)

    window.close()

if __name__ == "__main__":
    main()