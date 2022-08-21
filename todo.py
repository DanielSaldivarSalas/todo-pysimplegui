from typing import Any
import PySimpleGUI as sg
from file_functions import create_or_read_from_file, append_to_file, overwrite_file
from layouts import Layout



            
todo_tasks = create_or_read_from_file("todo_tasks.txt")

completed_tasks = create_or_read_from_file("completed_tasks.txt")

today_layout = Layout("Today").layout
personal_layout = Layout("Personal").layout
work_layout = Layout("Work").layout
immigration_layout = Layout("Immigration").layout
learning_layout = Layout("Learning").layout

tab_group = [
    [sg.TabGroup([[
        sg.Tab("Today", today_layout),
        sg.Tab("Personal", personal_layout),
        sg.Tab("Work", work_layout),
        sg.Tab("Immigration", immigration_layout),
        sg.Tab("Learning", learning_layout)
    ]])]
]
def has_user_pressed_closed_button(event: Any) -> bool:
    return event == sg.WIN_CLOSED

window = sg.Window('Todo App', tab_group)

while True:
    event, values = window.read()  # type: ignore
    
    if has_user_pressed_closed_button(event):
        break
    
    elif event == "add_save":
        todo_item: str = values["todo_item"]
        if todo_item:
            todo_tasks.append(todo_item) # type: ignore
            window['-TODO_TASKS-'].update(values=todo_tasks) # type: ignore
            append_to_file("todo_tasks.txt", todo_item) # type: ignore
            window["todo_item"].update("") # type: ignore
        
    elif event == "Button":
        window['-TEXT-'].update(values["-INPUT-"]) # type: ignore


    elif event == "Test Button":
        if values["-SPIN-"] == "item2":
            window["-TEST-"].update(visible = False) # type: ignore
    
    elif event == 'Complete':
        completed_task: str = values['-TODO_TASKS-'][0]
        
        todo_tasks.remove(completed_task) # type: ignore
        completed_tasks.append(completed_task) # type: ignore
        
        window['-TODO_TASKS-'].update(values=todo_tasks) # type: ignore
        overwrite_file("todo_tasks.txt", todo_tasks)
        window['-COMPLETED_TASKS-'].update(values=completed_tasks) # type: ignore

        append_to_file("completed_tasks.txt", completed_task)
        
    elif event == '-COMPLETED_DELETE-':
        completed_task:str = values["-COMPLETED_TASKS-"][0]
        completed_tasks.remove(completed_task)
        window["-COMPLETED_TASKS-"].update(values=completed_tasks) # type: ignore
        overwrite_file("completed_tasks.txt", completed_tasks)
        
    elif event == '-TODO_DELETE-':
        todo_task:str = values["-TODO_TASKS-"][0]
        todo_tasks.remove(todo_task)
        window["-TODO_TASKS-"].update(values=todo_tasks) # type: ignore
        overwrite_file("todo_tasks.txt", todo_tasks)
        
        
window.close()
