from task.Task import Task 

class Todo(Task):
    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return "{Todo: " + self.description + '}'
