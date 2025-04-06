##  create a class named Task which models a single task in a software company’s list of tasks.

##CODIGO CORRETO E ORGANIZADO
class Task:

    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.__id__counter()
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False  # Default value is False

    def __str__(self):
        return f"Task(id={self.id}, description='{self.description}', programmer='{self.programmer}', workload={self.workload}, finished={self.finished})"

    def __repr__(self):
        return f"Task({self.id}, '{self.description}', '{self.programmer}', {self.workload}, {self.finished})"

    def is_finished(self):
        """
        Returns True if the task is finished, False otherwise.
        """
        return self.finished

    def mark_finished(self):
        """
        Marks the task as finished.
        """
        self.finished = True

    @staticmethod
    def __id__counter():
        """
        Class method to generate unique IDs for each task.
        """
        if not hasattr(Task, "_id_counter"):
            Task._id_counter = 0
        Task._id_counter += 1
        return Task._id_counter




# Test the Task class
# Create a Task instance    
t1 = Task ("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished ()
print (t1)
print(t1.is_finished())
t2 = Task ("program webstone", "Adele", 10)
t3 = Task ("program mobile app for workload accounting", "Enic", 25)
print (t2)
print (t3)


## write a class named OrderBook that collects all the tasks ordered from a software company. The tasks should be created using the Task class you implemented in Part 1. 

class OrderBook:
    def __init__(self):
        self.tasks = []  # List to store tasks
        self.finished_tasks = []  # List to store finished tasks
        self.unfinished_tasks = [] # List to store unfinished tasks
        self.total_workload = 0 # Total workload of all tasks
        self.total_finished_workload = 0 # Total workload of finished tasks
        self.total_unfinished_workload = 0 # Total workload of unfinished tasks
        self.total_programmers = 0 # Total number of programmers
        self.total_tasks = 0 # Total number of tasks
        self.total_finished_tasks = 0 # Total number of finished tasks
        self.total_unfinished_tasks = 0 # Total number of unfinished tasks
    
    def add_task(self, task: Task):
        """
        Adds a task to the order book.
        """
        self.tasks.append(task)
        self.total_workload += task.workload
        self.total_tasks += 1
        self.total_programmers += 1 if task.programmer not in [t.programmer for t in self.tasks] else 0
        self.unfinished_tasks.append(task)
        self.total_unfinished_workload += task.workload
        self.total_unfinished_tasks += 1
        
    def finish_task(self, task_id: int):
        """
        Marks a task as finished and updates the order book.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                self.finished_tasks.append(task)
                self.unfinished_tasks.remove(task)
                self.total_finished_workload += task.workload
                self.total_unfinished_workload -= task.workload
                self.total_finished_tasks += 1
                self.total_unfinished_tasks -= 1
                break
        else:
            print(f"Task with ID {task_id} not found.") 
    
    def get_finished_tasks(self):
        """
        Returns a list of finished tasks.
        """
        return [task for task in self.tasks if task.is_finished()]
    
    def get_unfinished_tasks(self):
        """
        Returns a list of unfinished tasks.
        """
        return [task for task in self.tasks if not task.is_finished()]
    
    def get_total_workload(self):
        """
        Returns the total workload of all tasks.
        """
        return self.total_workload
    
    def get_total_finished_workload(self):
        """
        Returns the total workload of finished tasks.
        """
        return self.total_finished_workload
    
    def get_total_unfinished_workload(self):
        """
        Returns the total workload of unfinished tasks.
        """
        return self.total_unfinished_workload
    
    def get_total_programmers(self):
        """
        Returns the total number of programmers.
        """
        return self.total_programmers   
    
    def get_total_tasks(self):
        """
        Returns the total number of tasks.
        """
        return self.total_tasks
    
    def get_total_finished_tasks(self):
        """
        Returns the total number of finished tasks.
        """
        return self.total_finished_tasks
    
    def get_total_unfinished_tasks(self):
        """
        Returns the total number of unfinished tasks.
        """
        return self.total_unfinished_tasks
    
## implement a method to return a list of programmers that are task owners
    ## Implement a new method that returns a dictionary of key-value pairs,
    ## with keys corresponding to the names of the different programmers
    ## values corresponding to the list of task identifiers that are assigned to them.

    def get_programmers_tasks(self):
        """
        Returns a dictionary of programmers and their assigned tasks.
        """
        programmers_tasks = {}
        for task in self.tasks:
            if task.programmer not in programmers_tasks:
                programmers_tasks[task.programmer] = []
            programmers_tasks[task.programmer].append(task.id)
        return programmers_tasks    
    
    ## A method that takes the id of the task as its argument and marks the relevant task as finished. 
        ## If there is no task for the given id, the method should raise a ValueError exception.
•   ## A method that returns a list of the finished tasks from the OrderBook.
•   ## A method that returns a list of the unfinished tasks from the OrderBook.

def __str__(self):  
        """
        Returns a string representation of the OrderBook.
        """
        return f"OrderBook(tasks={self.tasks}, finished_tasks={self.finished_tasks}, unfinished_tasks={self.unfinished_tasks})"

def __repr__(self):
        """"
        "Returns a string representation of the OrderBook.
        """ 
        return f"OrderBook({self.tasks}, {self.finished_tasks}, {self.unfinished_tasks})"


## ALTEREI A ESTRUTUTA DO CODIGO PRA FICAR COMO O HANNA PEDIU
 ## SO PEGAR PARTE DO CODIGO QUE TINHA FEITO ANTES E USAR AQUI


## codigo organizado e correto até agr

## cod exercicio 1
## so funciona se for na msm celula, se for usar import ele nao reconhece

class Task:
    _id_counter = 0

    def __init__(self, description: str, programmer: str, workload: int):
        Task._id_counter += 1
        self.id = Task._id_counter
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    def __repr__(self):
        return self.__str__()

## classe nova, cod 2 pensando no resultado que o Hanna pediu
class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.tasks.append(task)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        names = []
        for task in self.tasks:
            if task.programmer not in names:
                names.append(task.programmer)
        return names

    ## Cod ex 3
    def get_programmers_tasks(self):
        """
        Returns a dictionary of programmers and their assigned tasks.
        """
        programmers_tasks = {}
        for task in self.tasks:
            if task.programmer not in programmers_tasks:
                programmers_tasks[task.programmer] = []
            programmers_tasks[task.programmer].append(task.id)
        return programmers_tasks    
    
    ## Cod ex 4
    def mark_finished(self, task_id):
        ## mesmo nome do metodo na task mas dif, tentei chamar o anterior mas deu erro e entendi
        ## procura uma tarefa específica dentro da lista (self.tasks) pelo ID
            ## quando encontrar, chama o mark_finished() da tarefa.
        
        """
        Marks the task with given id as finished. Raises ValueError if not found.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                return
        raise ValueError(f"No task with id {task_id} found")

    def finished_tasks(self):
        """
        Returns a list of finished tasks.
        """
        return [task for task in self.tasks if task.is_finished()]

    def unfinished_tasks(self):
        """
        Returns a list of unfinished tasks.
        """
        return [task for task in self.tasks if not task.is_finished()]
    
    