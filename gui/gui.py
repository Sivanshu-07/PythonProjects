import FreeSimpleGUI as sg
# 1 -> Simple Window App 

# layout = [
#     [sg.Text("Welcome! Sivanshu")],
#     [sg.Button("Exit")]
# ]
# window = sg.Window("Simple Window App",layout)

# while True:
#     event,values = window.read()

#     if event == sg.WINDOW_CLOSED or event == "Exit":
#         break
# window.close()

# 2 Name Input App

# layout = [
#     [sg.Text("Enter Your Name",font=("Ariel",12,"bold"))],
#     [sg.Input(key="Name")],
#     [sg.Button("Submit")],
#     [sg.Text("",size = (20,1),key="Result")]
# ]
# window = sg.Window("Name Input App",layout)

# while True:
#     event,values = window.read()

# # values ek dictionary hoti hai jisme input box ka data stored hota hai
#         # "Name ek key hai toh key pass kiya toh value return krega jo ki input box me jo likha hai wo hai"

#     if event == sg.WINDOW_CLOSED:
#         break

#     if event == "Submit": # button ka text hi event hota hai
#         name = values["Name"] 
#         if name.strip() == "": # strip() faltu ke spaces hata deta hai
#             sg.popup_error("Please enter your name first!")
#         else :
#             window["Result"].update(f"Hello, {name}")

# window.close()
        
# 3

# layout = [
#     [sg.Text("Enter Password")],
#     [sg.Input(key="pwd",password_char='*')],
#     [sg.Button("Show"),sg.Button("Exit")]
# ]
# window = sg.Window("Show/Hide Password UI",layout)

# hidden = True

# while True:
#     event,values = window.read()

#     if event == sg.WINDOW_CLOSED or event == "Exit":
#         break

#     if event == "Show":
#         if hidden:
#             window["pwd"].update(password_char="")
#             hidden = False
#         else :
#             window["pwd"].update(password_char="*")
#             hidden = True
        
# window.close()

# 4
# layout = [[sg.Text("Enter First Number"),sg.Input(key="a")],
#     [sg.Text("Enter Second Number"),sg.Input(key="b")],

#     [sg.Button("Add"),sg.Button("Exit")],
#     [sg.Text("",key="Result")]
# ]
# window = sg.Window("Simple Calculator UI(Only Add)",layout)

# while True:
#     event ,values = window.read()
#     if event == sg.WINDOW_CLOSED or event =="Exit":
#         break
#     if event == "Add":
#         x = int(values["a"]) # ye string hai isko int me typecast krna padega
#         y = int(values["b"])
#         window["Result"].update(f"Sum of {x} + {y} = {x+y}")
# window.close()

# 5

# layout = [
#     [sg.Text("Enter Your Name"),sg.Input()],
#     [sg.Text("Enter Your Email"),sg.Input()],
#     [sg.Input(size=(20,2))],
#     [sg.Button("Submit"),sg.Button("Exit")]
# ]
# window = sg.Window("Feedback Form UI",layout)

# while True:
#     event ,values = window.read()

#     if event == sg.WINDOW_CLOSED or event == "Exit":
#         break
#     if event == "Submit":
#         sg.popup("Feedback Submitted")
# window.close()

# 6

themes = sg.theme_list()

layout = [
    [sg.Text("Select Theme")],
    [sg.Combo(themes,key = "Theme")],
    [sg.Button("Apply")]
]
window = sg.Window("Theme Changer", layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event =="Apply":
        sg.theme(values["Theme"])
        sg.popup("Restart App to apply theme")
window.close()