# classes.py

class Task:
    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.__id__counter()
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    def __repr__(self):
        return self.__str__()

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    @staticmethod
    def __id__counter():
        if not hasattr(Task, "_id_counter"):
            Task._id_counter = 0
        Task._id_counter += 1
        return Task._id_counter


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.tasks.append(task)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list({task.programmer for task in self.tasks})

    def get_programmers_tasks(self):
        programmers_tasks = {}
        for task in self.tasks:
            if task.programmer not in programmers_tasks:
                programmers_tasks[task.programmer] = []
            programmers_tasks[task.programmer].append(task.id)
        return programmers_tasks

    def mark_finished(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                return
        raise ValueError(f"No task with id {task_id} found")

    def finished_tasks(self):
        return [task for task in self.tasks if task.is_finished()]

    def unfinished_tasks(self):
        return [task for task in self.tasks if not task.is_finished()]

    def status_of_programmer(self, name):
        if name not in self.programmers():
            raise ValueError("No such programmer")

        finished = [task for task in self.tasks if task.programmer == name and task.is_finished()]
        unfinished = [task for task in self.tasks if task.programmer == name and not task.is_finished()]

        return (
            len(finished),
            len(unfinished),
            sum(task.workload for task in finished),
            sum(task.workload for task in unfinished),
        )
