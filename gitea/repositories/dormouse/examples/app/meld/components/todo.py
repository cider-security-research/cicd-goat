from flask_meld.component import Component


class Todo(Component):
    todo = ""
    todos = []
    completed_todos = []
    edit_todo_index = None
    updated_todo = ""

    def add_todo(self):
        if self.todo:
            self.todos.append(self.todo)
            self.todo = ""

    def complete_todo(self, index):
        todo = self.todos.pop(index)
        self.completed_todos.append(todo)

    def remove_todo(self, index):
        self.todos.pop(index)

    def set_edit_todo(self, index):
        self.edit_todo_index = index
        self.updated_todo = self.todos[index]

    def edit_todo(self):
        self.todos[self.edit_todo_index] = self.updated_todo
        self.edit_todo_index = None

    def undo(self, index):
        todo = self.completed_todos.pop(index)
        self.todos.append(todo)
