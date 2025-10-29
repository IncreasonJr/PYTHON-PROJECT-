class Todolist:
    def __init__(self):
        self.tasks=[]

    def add_task(self,new_task):
        self.tasks.append(new_task)
        print('Task added')

    def view_task(self):
        if self.tasks==[]:
            print('No task added yet')
        else:
            for task in self.tasks:
               print(self.tasks)


    def remove_task(self,number):
        self.tasks.pop(number)
        print("task removed")


def main():
    todo=Todolist()

    while True:
        print('This is your todo list.')
        print('1.Add Task')
        print('2.View Task')
        print('3. Remove Task')
        print('4. Exit')
        choice = input('Enter your choice(1-4): ')

        if choice=='1':
            new_task=input('Enter task to add: ')
            todo.add_task(new_task)
        elif choice=='2':
            todo.view_task()
        elif choice=='3':
            todo.view_task()
            number=int(input('Enter the number of the task you want to remove: '))
            todo.remove_task(number)
        elif choice=='4':
            break
        else:
            print('Invalid choice. Choose from 1-4')

main()

