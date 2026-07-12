
file_name = '/home/firas/private-projects/task-tracker-practice/python/content.txt'

def get_tasks():
    try:
        with open(file_name) as file:
            return file.read().splitlines()
    except:
        FileNotFoundError

def add_task(task):
    task_id = 1
    tasks = get_tasks()
    if tasks:
        print(f'tasks: {tasks}')
        for t in tasks:
            element = t.split(' - ', 1)
            id = int(element[0])
            task_id = id + 1
    else:
        task_id
    with open(file_name, 'a') as file:
        entry = f'{task_id} - {task}\n'
        file.write(entry)
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
            
def update_task_list(tasks):
    with open(file_name, 'w') as file:
        content = '\n'.join(tasks)
        file.write(content)

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



