from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class task:
    title:str
    description:str
    status: Literal["todo","in_progress","done"]
    due_date:date | None=None

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("title cannot be empty")
        
        if self.due_date and self.due_date < date.today():
            raise ValueError('due date cannot be in the past')
        

    def advance_status(self):
        if self.status == "todo":
            self.status="in_progress"
        elif self.status=="in_progress":
            self.status="done"
        