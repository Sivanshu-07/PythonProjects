import FreeSimpleGUI as sg
from zip_make import ZipCreate

layout = [
    [sg.Text("Select Files to Compress",font=("Ariel",12,"bold"))],
    [
        sg.Button("Choose Files",key="browsefile"),
        sg.Input(size=(40,1),key="file") # input is like a dictionary 
    ],
    [sg.Text("Select Destination Folder")],
    [
        sg.Button("Choose Folder",key="browsefolder"),
        sg.Input(size=(40,1),key="folder")
    ],
    [sg.Push(),sg.Button("Compress",size=(20,1)),sg.Push()]
]

window = sg.Window("File Compressor App",layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "browsefile":
        files = sg.popup_get_file("Select Files",multiple_files = True)
        if files:
            window["file"].update(files)

    if event == "browsefolder":
        folder = sg.popup_get_folder("Select Folder")
        if folder:
            window["folder"].update(folder)

    if event == "Compress":
        if not values["file"]:
            sg.popup("Please Select Files First")
            continue
        if not values["folder"]:
            sg.popup("Please Select Destination Folder")
            continue
        
        filePaths = values["file"].split(";")
        folder = values["folder"]

        ZipCreate(filePaths,folder)

        sg.popup("Compression Successfull")
window.close()