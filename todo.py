from typing import Any
import PySimpleGUI as sg
from file_functions import append_to_file, overwrite_file
from layouts import Category

sg.set_options(font= "Calibri 15")

today_category: Category = Category("today")
personal_category = Category("personal")
work_category = Category("work")
immigration_category = Category("immigration")
learning_category = Category("learning")

tab_group = [
    [sg.TabGroup([[
        sg.Tab("Today", today_category.layout),
        sg.Tab("Personal", personal_category.layout),
        sg.Tab("Work", work_category.layout),
        sg.Tab("Immigration", immigration_category.layout),
        sg.Tab("Learning", learning_category.layout)
    ]])]
]
def has_user_pressed_closed_button(event: Any) -> bool:
    return event == sg.WIN_CLOSED

window = sg.Window('Todo App', tab_group)
class CategoryFactory:
    @staticmethod
    def category(category:str):
        match category:
            case "today":
                return today_category
            case "personal":
                return personal_category
            case "work":
                return work_category
            case "immigration":
                return immigration_category
            case "learning":
                return learning_category
            case _:
                pass
        
while True:
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED:
        break
    category_name: str = ''.join([c for c in event.split("_")[0].lower() if c.isalpha()]) # type: ignore
    category_instance = CategoryFactory.category(category_name)
    
    match event:
        
        case "today_add_save"| "personal_add_save" | "work_add_save" | "immigration_add_save" | "learning_add_save":
            #category = event.split("_")[0]
            
            todo_item: str = values[f"{category_name}_todo_item"]
            print(f"{todo_item=}")
            if todo_item:
                category_instance.todo_tasks.append(todo_item) # type: ignore
                #today_category.todo_tasks.append(todo_item)
               # todo_tasks.append(todo_item) # type: ignore
                window[f'-{category_name.upper()}_TODO_TASKS-'].update(values=category_instance.todo_tasks) # type: ignore
                append_to_file(f"{category_name}_todo_tasks.txt", todo_item) # type: ignore
                window[f"{category_name}_todo_item"].update("") # type: ignore
                
        case "today_complete" | "personal_complete"| "work_complete" | "immigration_complete"| "learning_complete":
            completed_task: str = values[f'-{category_name.upper()}_TODO_TASKS-'][0]
           
            category_instance.todo_tasks.remove(completed_task) # type: ignore
            #todo_tasks.remove(completed_task) # type: ignore
            category_instance.completed_tasks.append(completed_task) # type: ignore
            #completed_tasks.append(completed_task) # type: ignore
        
            window[f'-{category_name.upper()}_TODO_TASKS-'].update(values=category_instance.todo_tasks) # type: ignore
            overwrite_file(f"{category_name}_todo_tasks.txt", category_instance.todo_tasks) # type: ignore
            window[f'-{category_name.upper()}_COMPLETED_TASKS-'].update(values=category_instance.completed_tasks) # type: ignore

            append_to_file(f"{category_name}_completed_tasks.txt", completed_task)
            
        case "-TODAY_COMPLETED_DELETE-"| "-PERSONAL_COMPLETED_DELETE-"| "-WORK_COMPLETED_DELETE-" | '-IMMIGRATION_COMPLETED_DELETE-' | '-LEARNING_COMPLETED_DELETE-':
            completed_task:str = values[f"-{category_name.upper()}_COMPLETED_TASKS-"][0]
            category_instance.completed_tasks.remove(completed_task)    # type: ignore
            window[f"-{category_name.upper()}_COMPLETED_TASKS-"].update(values=category_instance.completed_tasks) # type: ignore
            overwrite_file(f"{category_name}_completed_tasks.txt", category_instance.completed_tasks) # type: ignore
        
        case "-TODAY_TODO_DELETE-"| "-PERSONAL_TODO_DELETE-"| "-WORK_TODO_DELETE-"| "-IMMIGRATION_TODO_DELETE-"| "-LEARNING_TODO_DELETE-":    
            todo_task:str = values[f"-{category_name.upper()}_TODO_TASKS-"][0]
            category_instance.todo_tasks.remove(todo_task) # type: ignore
            
            window[f"-{category_name.upper()}_TODO_TASKS-"].update(values=category_instance.todo_tasks) # type: ignore
            overwrite_file(f"{category_name}_todo_tasks.txt", category_instance.todo_tasks) # type: ignore

        case _:
            pass
        
        
window.close()
