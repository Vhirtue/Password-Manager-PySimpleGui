import PySimpleGUI as sg

# Define the column headings and values
headings = ['Column 1', 'Column 2', 'Column 3']
data = [['Row 1', 'Value 1', 'Value 2'],
        ['Row 2', 'Value 3', 'Value 4'],
        ['Row 3', 'Value 5', 'Value 6']]

# Create the layout with the table
layout = [
    [sg.Table(values=data, headings=headings, auto_size_columns=False, justification='left', key='-TABLE-')],
    [sg.Button('Get Selected Row'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Table Example', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Get Selected Row':
        # Get the index of the selected row
        selected_row = values['-TABLE-'][0]
        # Get the data of the selected row
        selected_row_data = data[selected_row]
        print(f"Selected Row Data: {selected_row_data}")

# Close the window
window.close()
