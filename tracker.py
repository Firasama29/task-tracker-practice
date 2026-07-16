import python.tasks_activities as tasks
import sys
from python.exceptions import TaskNotFoundError, InvalidTaskIdError


command = sys.argv[1]

activity = 'Add a new task: 1\n' \
'View all tasks: 2\n' \
'Update a task: 3\n' \
'Delete a task: 4\n' \
'Mark as in-progress: 5\n' \
'Mark as completed: 6\n' \
'Check pending/in-progress tasks: 7\n' \
'Check completed tasks: 8'

# print(f"choose a task:\n{activity}")

# choice = input()

# list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def read_task_id():
    try:
        return int(input())
    except ValueError:
        raise InvalidTaskIdError("task id must be a number")

if __name__ == '__main__':
    task_list = tasks.get_tasks()
    if command == "add":
        task = input("add a task: ")
        tasks.add_task(task)

    elif command == "list":
        print(f'tasks retrieved:\n{task_list}')

    elif command == "update":
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you want to update:")
        task_id = read_task_id()
        if not any(task_id == int(t["id"]) for t in task_list):
            raise TaskNotFoundError(f"Task not found with id {task_id}")
        requested_task = input("enter the new task: ")
        tasks.update_task(task_id, requested_task)

    elif command == "delete":
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you want to delete:")
        task_id = read_task_id()
        if not any(task_id == int(t["id"]) for t in task_list):
            raise TaskNotFoundError(f"Task not found with id {task_id}")
        tasks.delete_task(task_id)

    elif command == "progress":
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you're working on:")
        task_id = read_task_id()
        if not any(task_id == int(t["id"]) for t in task_list):
            raise TaskNotFoundError(f"Task not found with id {task_id}")
        tasks.mark_in_progress(task_id)

    elif command == "completed":
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you completed:")
        task_id = read_task_id()
        if not any(task_id == int(t["id"]) for t in task_list):
            raise TaskNotFoundError(f"Task not found with id {task_id}")
        tasks.mark_completed(task_id)

    elif command == "pending":
        incomplete_tasks = tasks.filter_incomplete_tasks()
        print(f"pending tasks:\n{incomplete_tasks}")

    elif command == "done":
        completed_tasks = tasks.filter_completed_tasks()
        print(f"completed tasks:\n{completed_tasks}")