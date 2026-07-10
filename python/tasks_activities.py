
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

