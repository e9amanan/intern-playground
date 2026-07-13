"""Inheritance

    Create base Task class and inherit UrgentTask subclass
    Method overriding and super()
    When to use inheritance vs composition

Composition over inheritance

    Example: TaskManager that contains a list of Task objects

"""

class task:
    def __init__(self,title:str):
        self.title=title
        self.completed=False

    def display(self) -> str:
        return f"task: {self.title}"

class urgenttask(task):
    def __init__(self,title:str,deadline:str):
        super().__init__(title)
        self.deadline=deadline

    def display(self)->str:
        base_display=super().display()
        return f"{base_display} (DUE:{self.deadline})"

class taskmanager:

    def __init__(self):
        self._tasks: list =[]

    def add_tasks(self,task):
        self._tasks.append(task)

    def get_pending_tasks(self)->list:
        return [t for t in self._tasks if getattr(t, 'status','')!= "done"]
    


    