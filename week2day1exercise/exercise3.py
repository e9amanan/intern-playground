class Task:
    def __init__(self,title:str,description:str):
        self.title=title
        self.description=description
        self.completed=False

    def mark_complete(self)-> None:
        self.completed=True

    def __repr__(self)->str:
        status = '✓' if self.completed else "o"
        return f"{status}{self.title}"
    
class UrgentTask(Task):

    def __init__(self,title:str,description:str,deadline:str):
        super().__init__(title,description)
        self.deadline=deadline

    def is_overdue(self,current_date:str)-> bool:
        return self.deadline>current_date
    
    def __repr__(self)-> str:
        base = super().__repr__()
        return f"{base} (Due: {self.deadline})"
    

