import PySimpleGUI as sg
from file_functions import create_or_read_from_file
from typing import Any
smileys = [ 
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
    
]

menu_layout = [
    ["File", ['Open', 'Save', '---', 'Exit']],
    ["Tools", ["Word Count"]],
    ["Add", smileys]
]


todo_tasks = create_or_read_from_file("todo_tasks.txt")

completed_tasks = create_or_read_from_file("completed_tasks.txt")


class Layout:
    
    def __init__(self, name: str) -> None:
        self.layout: list[Any] = []
       # self.layout.append(sg.Menu(menu_layout))
        self.layout.append([sg.Text("Todo")])
        self.layout.append([sg.InputText("", key="todo_item"), sg.Button(button_text="Add", key="add_save")])
        self.layout.append([sg.Text("Todo List")])
        self.layout.append([sg.Listbox(values=todo_tasks, size=(40,15), key="-TODO_TASKS-"),sg.Button("Complete"), sg.Button("Delete", key="-TODO_DELETE-"), sg.Button("Edit")])
        self.layout.append([sg.Text("Completed List")])
        self.layout.append([sg.Listbox(values=completed_tasks, size=(40,15), key="-COMPLETED_TASKS-"),sg.Button("Delete", key='-COMPLETED_DELETE-')])
