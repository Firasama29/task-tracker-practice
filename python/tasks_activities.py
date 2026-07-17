import json
from .exceptions import TaskDataCorruptedError

file_name = '/home/firas/private-projects/task-tracker-practice/python/content.json'

def get_tasks():
    try:
        with open(file_name) as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise TaskDataCorruptedError("content.json is corrupted")

def add_task(task):
    task_id = 1
    tasks = get_tasks() if get_tasks() else []
    if tasks:
        task_id = max((t["id"] for t in tasks), default=0) + 1
        add_new_task(tasks, task, task_id)
    else:
        tasks = []
        add_new_task(tasks, task, task_id)

def update_task(task_id, new_task):
    tasks = get_tasks() if get_tasks() else []
    for task in tasks:
        if task_id == int(task["id"]):
            print(f"task: {task}")
            task["task"] = new_task
            update_task_list(tasks)
            print(f'updated task: {task}')
            break

def delete_task(task_id):
    tasks = get_tasks() if get_tasks() else []
    print(f'tasks: {tasks}')
    for task in tasks:
        if task_id == int(task["id"]):
            tasks.remove(task)
            print(f'removed task: {task}')
            update_task_list(tasks)
    print(f'tasks: {tasks}')

def mark_in_progress(task_id):
    tasks = get_tasks() if get_tasks() else []
    for task in tasks:
        if task_id == int(task["id"]):
            task['status'] = 'in-progress'
            update_task_list(tasks)
            print(f'updated task: {task}')

def mark_completed(task_id):
    tasks = get_tasks() if get_tasks() else []
    for task in tasks:
        if task_id == int(task["id"]):
            task['status'] = 'done'
            update_task_list(tasks)
            print(f'updated task: {task}')

def filter_incomplete_tasks():
    tasks = get_tasks()
    filtered_tasks = []
    for task in tasks:
        status = task['status']
        if status not in ['done']:
            filtered_tasks.append(task)
    return filtered_tasks

def filter_completed_tasks():
    tasks = get_tasks()
    filtered_tasks = []
    for task in tasks:
        status = task['status']
        if status in ['done']:
            filtered_tasks.append(task)
    return filtered_tasks

def add_new_task(tasks, task, task_id):
    with open(file_name, 'w') as file:
        entry = {"id": task_id, "task": task, "status": 'pending'}
        tasks.append(entry)
        json.dump(tasks, file, indent=2)
        print(f'task added: {entry}')

def update_task_list(tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=2)
