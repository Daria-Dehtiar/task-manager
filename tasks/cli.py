from .storage import add_task, remove_task, get_all_tasks, mark_task_completed
from .export import save_to_file
def handle_action():
    user_input = input('What action do you want to take?\n'
                       '1. Add a new task\n'
                       '2. Remove a task\n'
                       '3. Mark as done\n'
                       '4. Show all tasks\n')
    match user_input:
        case '1':
            title = input('What is the title of the task? ')
            add_task(title)
        case '2':
            print(get_all_tasks())
            index = int(input('Choose task index to remove '))
            remove_task(index)
        case '3':
            print(get_all_tasks())
            index = int(input('Choose task index to mark as done '))
            mark_task_completed(index, True)
        case '4':
            print(get_all_tasks())
        case _:
            print('Try again')

    print(user_input)

def handle_interrupt():
    user_input = input('\nDo you want to export tasks (y/n)? ')
    if user_input == "y":
        save_to_file(get_all_tasks(), 'export')
        return True

