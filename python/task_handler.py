import tasks_activities as tasks

activity = 'Add a new task: 1\n' \
'View all tasks: 2\n' \
'Update a task: 3\n' \
'Delete a task: 4'

print("choose a task:")

choice = input()

list = ['1', '2', '3', '4']

if __name__ == '__main__':
    task_list = tasks.get_tasks()
    if choice == list[0]:
        task = input("add a task: ")
        tasks.add_task(task)
    elif choice == list[1]:
        print(f'tasks retrieved:\n{task_list}')
    elif choice == list[2]:
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you want to update:")
        task_id = int(input())
        requested_task = input("enter the new task: ")
        tasks.update_task(task_id, requested_task)
    elif choice == list[3]:
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you want to delete:")
        task_id = int(input())
        tasks.delete_task(task_id)