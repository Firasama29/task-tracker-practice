import tasks_activities as tasks

activity = 'Add a new task: 1\n' \
'View all tasks: 2\n' \
'Update a task: 3\n' \
'Delete a task: 4'

print("choose a task:")

choice = input()

list = ['1', '2', '3', '4']

if __name__ == '__main__':
    if choice == list[0]:
        task = input("add a task: ")
        tasks.add_task(task)
    elif choice == list[1]:
        task_list = tasks.get_tasks()
        print(f'tasks retrieved:\n{task_list}')