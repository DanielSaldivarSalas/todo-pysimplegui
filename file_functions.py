from genericpath import exists
from os.path import exists

def _read_from_file(fname: str) -> list[str]:
    
 
    tasks: list[str] = []
    with open(fname) as f:
        lines: list[str] = f.readlines()
        print(lines)
        for line in lines:
            tasks.append(line.rstrip("\n"))
        
    return tasks

def _create_file(fname: str) -> None:
    
    with open(fname, "w") as f:
        print(f"{fname} file has been created")
    
def create_or_read_from_file(fname: str) -> list[str] :
    fname = f"data/{fname}"
    if exists(fname):
        print("file exists")
        return _read_from_file(fname)
    else:
        print("File does not exist")
        _create_file(fname)
        return []
    
def append_to_file(fname: str, task: str) -> None:
    fname = f"data/{fname}"
    with open(fname, "a") as f:
        f.write(f"{task}\n")

def overwrite_file(fname: str, tasks: list[str]) -> None:
    fname = f"data/{fname}"
    with open(fname, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")