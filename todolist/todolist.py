from todo import Todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def __str__(self):
        return '\n'.join([f"----- {self.title} -----"] + [str(todo) for todo in self._todos])

    def __len__(self):
        return len(self._todos)

    def add(self, other):
        if not isinstance(other, Todo):
            raise TypeError

        self._todos.append(other)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def to_list(self):
        return self._todos.copy()

    def todo_at(self, idx):
        return self._todos[idx]

    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def mark_all_done(self):
        for todo in self._todos:
            todo.done = True

    def mark_all_undone(self):
        for todo in self._todos:
            todo.done = False

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def remove_at(self, idx):
        self._todos.pop(idx)

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        todolist = TodoList(self.title)
        def choose(todo):
            if callback(todo):
                todolist.add(todo)

        self.each(choose)
        return todolist

    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        self.find_by_title(title).done = True

    def mark_undone(self, title):
        self.find_by_title(title).done = False