from typing import Any
import PySimpleGUI as sg

layout = [
    [sg.Text("Text"), sg.Spin(["item1", "item 2"])],
    [sg.Button("Button")], 
    [sg.Input()]
]

def has_user_pressed_closed_button(event: Any) -> bool:
    return event == sg.WIN_CLOSED


window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if has_user_pressed_closed_button(event):
        break


window.close()
