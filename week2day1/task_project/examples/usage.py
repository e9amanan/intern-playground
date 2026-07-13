from datetime import date,timedelta
from features.models import task
from core.manager import taskmanager

def main():
    manager = taskmanager()

    task1=task(
        title="Complete OOP Exercise",
        description="finish day 1 syllabus",
        status="todo",
        due_date=date.today() + timedelta(days=1)
    )

    task2=task(
        title="review Leetcode",
        description="merge sorted lists",
        status="in_progress"
    )

    manager.add_task(task1)
    manager.add_task(task2)

    task1.advance_status()

    pending=manager.get_pending_tasks()
    print(f"pending tasks({len(pending)}):")
    for t in pending:
        print(f"- {t.title} [{t.status}]")

if __name__ == "__main__":
    main()