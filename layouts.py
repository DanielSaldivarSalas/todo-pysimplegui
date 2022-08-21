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



class Category:
    
    def __init__(self, name: str) -> None:
        self.todo_tasks: list[Any] = create_or_read_from_file(f"{name}_todo_tasks.txt")

        self.completed_tasks = create_or_read_from_file(f"{name}_completed_tasks.txt")
        
        self.layout: list[Any] = []
       # self.layout.append(sg.Menu(menu_layout))
        self.layout.append([sg.Text("Todo")])
        self.layout.append([sg.InputText("", key=f"{name}_todo_item"), sg.Button(button_text="Add", key=f"{name}_add_save")])
        self.layout.append([sg.Text("Todo List")])
        self.layout.append([sg.Listbox(values=self.todo_tasks, size=(50,15), key=f"-{name.upper()}_TODO_TASKS-"),sg.Button("Complete", key=f"{name}_complete"), sg.Button("Delete", key=f"-{name.upper()}_TODO_DELETE-"), sg.Button("Edit")])
        self.layout.append([sg.Text("Completed List")])
        self.layout.append([sg.Listbox(values=self.completed_tasks, size=(50,15), key=f"-{name.upper()}_COMPLETED_TASKS-"),sg.Button("Delete", key=f'-{name.upper()}_COMPLETED_DELETE-')])
