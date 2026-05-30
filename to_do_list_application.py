tasks =[]
def main():
    messege = """ 
    1-add task to list 
    2-mark tasks as complete 
    3-view tasks
    4-quit
    """
    while True:
        print(messege)
        choice = input('enter your choice : ')

        if choice == '1':
            add_task()
        elif choice== '2':
            mark_task_complete()
        elif choice== '3':
            view_tasks()
        elif choice== '4':
            break
        else:print('enter a valid choice ')     

def add_task():
    # get the task from user
    task = input('enter task : ')
    #define status of task
    task_info = {'task':task,'completed':False}
    #add task to list
    tasks.append(task_info)
    print('task added to the list successfully')
    print(task_info)

def mark_task_complete():
    incompleted_tasks = [task for task in tasks if task['completed'] == False]
    if  not incompleted_tasks :
        print('no tasks to mark as completed')
        return

    #show them to the use
    for i, task in enumerate(incompleted_tasks):
        print(f"{1+i}-{task['task']}")
    # get the task from the user
    task_number = int(input('enter the number of the task to complete'))
    #mark the task as completed
    incompleted_tasks[task_number - 1]['completed'] = True
    #print a message to user
    print(tasks)

def view_tasks():
    if not tasks:
        print('no tasks to view')
        return
    for i, task in enumerate(tasks):
        # if task['completed']:
        #     status = '✔'
        
        # else:
        #     status='🎗'
        status = '✔' if task['completed'] else '🎗'
        print(f"{1+i}.-{task['task']}{status}")
main()


    