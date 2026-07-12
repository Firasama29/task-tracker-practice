import tasks_activities as tasks

activity = 'Add a new task: 1\n' \
'View all tasks: 2\n' \
'Update a task: 3\n' \
'Delete a task: 4\n' \
'Mark as in-progress: 5\n' \
'Mark as completed: 6\n' \
'Check pending/in-progress tasks: 7\n' \
'Check completed tasks: 8'

print(f"choose a task:\n{activity}")

choice = input()

list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

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
    elif choice == list[4]:
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you're working on:")
        task_id = int(input())
        tasks.mark_in_progress(task_id)
    elif choice == list[5]:
        print(f'tasks retrieved:\n{task_list}')
        print("select the id of the task you completed:")
        task_id = int(input())
        tasks.mark_completed(task_id)
    elif choice == list[6]:
        incomplete_tasks = tasks.filter_incomplete_tasks()
        print(f"pending tasks:\n{incomplete_tasks}")
    elif choice == list[7]:
        completed_tasks = tasks.filter_completed_tasks()
        print(f"completed tasks:\n{completed_tasks}")