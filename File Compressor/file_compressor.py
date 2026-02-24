<<<<<<< HEAD
import FreeSimpleGUI as sg
from zip_maker import zipCreate

layout = [

    [sg.Text("Select Files to Compress", font=("Arial", 12, "bold"))],

    [
        sg.Button("Choose Files", key="browse_files"),
        sg.Input(size=(40,1), key="file")
    ],

    [sg.Text("Select Destination Folder", font=("Arial", 12, "bold"))],

    [
        sg.Button("Choose Folder", key="browse_folder"),
        sg.Input(size=(40,1), key="folder")
    ],

    [sg.Push(), sg.Button("Compress", size=(15,1)), sg.Push()] # push from the left and push from the right so that compress button will be at centre
]

window = sg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    print(event,values)

    if event == sg.WINDOW_CLOSED:
        break

    if event == "browse_files":
        files = sg.popup_get_file("Select Files",multiple_files=True)

        if files:
            window["file"].update(files)

    if event == "browse_folder":
        folder = sg.popup_get_folder("Select Folder")
        if folder:
            window["folder"].update(folder)

    if event == "Compress":

        if not values["file"]:
            sg.popup("Please select files first!")
            continue

        if not values["folder"]:
            sg.popup("Please select destination folder!")
            continue

        filePaths = values["file"].split(";")
        folder = values["folder"]

        zipCreate(filePaths, folder)

        sg.popup("Compression Successful!")


window.close()

=======
import FreeSimpleGUI as sg
from zip_maker import zipCreate

layout = [

    [sg.Text("Select Files to Compress", font=("Arial", 12, "bold"))],

    [
        sg.Button("Choose Files", key="browse_files"),
        sg.Input(size=(40,1), key="file")
    ],

    [sg.Text("Select Destination Folder", font=("Arial", 12, "bold"))],

    [
        sg.Button("Choose Folder", key="browse_folder"),
        sg.Input(size=(40,1), key="folder")
    ],

    [sg.Push(), sg.Button("Compress", size=(15,1)), sg.Push()]
]

window = sg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    print(event,values)

    if event == sg.WINDOW_CLOSED:
        break

    if event == "browse_files":
        files = sg.popup_get_file("Select Files",multiple_files=True)

        if files:
            window["file"].update(files)

    if event == "browse_folder":
        folder = sg.popup_get_folder("Select Folder")
        if folder:
            window["folder"].update(folder)

    if event == "Compress":

        if not values["file"]:
            sg.popup("Please select files first!")
            continue

        if not values["folder"]:
            sg.popup("Please select destination folder!")
            continue

        filePaths = values["file"].split(";")
        folder = values["folder"]

        zipCreate(filePaths, folder)

        sg.popup("Compression Successful!")

window.close()
>>>>>>> e0d4995 (Added Personal Expense Tracker Project)
