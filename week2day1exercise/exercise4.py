from exercise3 import Task

class TaskManager:
    
    def __init__(self):
        self.tasks:list[Task]=[]

    def add_task(self,task:Task)-> None:
        self.task.append(task)

    def get_incomplete_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]
    
    def get_complete_tasks(self) -> list[Task]:
        return [task for task in self.tasks if task.completed]
    
    def mark_task_complete(self,title:str)->bool:
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
            return False
        

    def __len__(self)->int:
        return len(self.tasks)
    
