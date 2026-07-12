import json

file_name = '/home/firas/private-projects/task-tracker-practice/python/content.json'

def get_tasks():
    try:
        with open(file_name) as file:
            return json.load(file)
    except:
        FileNotFoundError

def add_task(task):
    task_id = 1
    tasks = get_tasks() if get_tasks() else []
    if tasks:
        print(f'tasks1: {tasks}')
        task_id = max((t["id"] for t in tasks), default=0) + 1
        print(f'tasks: {tasks}')
        add_new_task(tasks, task, task_id)
    else:
        tasks = []
        add_new_task(tasks, task, task_id)
    
def add_new_task(tasks, task, task_id):
    with open(file_name, 'w') as file:
        print(f'tasks2: {tasks}')
        entry = {
            "id": task_id, 
            "task": task,
            "status": 'pending'
        }
        tasks.append(entry)
        print(f'new list: {tasks}')
        json.dump(tasks, file)
        print(f'task added: {entry}')

def update_task(task_id, new_task):
    tasks = get_tasks()
    print(f'tasks: {tasks}')
    updated_task = ''
    for task in tasks:
        id = int(task.split(' - ')[0])
        taskstr = task.split(' - ')[1]
        if task_id == id:
            updated_task = f'{id} - {taskstr.replace(taskstr, new_task)}'
            print(f'updated_task inside loop: {updated_task}')
            tasks[tasks.index(task)] = updated_task
            update_task_list(tasks)
    print(f'tasks: {tasks}')

def delete_task(task_id):
    tasks = get_tasks()
    print(f'tasks: {tasks}')
    for task in tasks:
        id = int(task.split(' - ')[0])
        if task_id == id:
            tasks.remove(task)
            print('removed a task')
            update_task_list(tasks)
    print(f'tasks: {tasks}')

def mark_in_progress(task_id):
    tasks = get_tasks()
    for task in tasks:
        id = int(task.split(' - ')[0])
        taskstr = task.split(' - ')[1]
        if task_id == id:
            updated_task = f'{id} - {taskstr} - in-progress'
            tasks[tasks.index(task)] = updated_task
            update_task_list(tasks)
    print(f'tasks: {tasks}')

def mark_completed(task_id):
    tasks = get_tasks()
    for task in tasks:
        id = int(task.split(' - ')[0])
        taskstr = task.split(' - ')[1]
        if task_id == id:
            updated_task = f'{id} - {taskstr} - done'
            tasks[tasks.index(task)] = updated_task
            update_task_list(tasks)
    print(f'tasks: {tasks}')

def filter_incomplete_tasks():
    tasks = get_tasks()
    filtered_tasks = []
    for task in tasks:
        status = task.split(' - ')[2]
        if status not in ['done']:
            filtered_tasks.append(task)
    return filtered_tasks

def filter_completed_tasks():
    tasks = get_tasks()
    filtered_tasks = []
    for task in tasks:
        status = task.split(' - ')[2]
        if status in ['done']:
            filtered_tasks.append(task)
    return filtered_tasks

def update_task_list(tasks):
    with open(file_name, 'w') as file:
        content = '\n'.join(tasks)
        file.write(content)