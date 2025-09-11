import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(1)
        with self.assertRaises(TypeError):
            self.todos.add('hi')

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        with self.assertRaises(IndexError):
            self.todos.todo_at(5)

    def test_mark_done_at(self):
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)

    def test_mark_undone_at(self):
        self.todos.mark_all_done()
        self.todos.mark_undone_at(0)
        self.todos.mark_undone_at(1)
        self.assertFalse(self.todo1.done)
        self.assertFalse(self.todo2.done)
        self.assertTrue(self.todo3.done)
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)

    def test_mark_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

    def test_remove_at(self):
        self.todos.remove_at(1)
        self.assertEqual([self.todo1, self.todo3], self.todos.to_list())

    def test_str(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[X] Go to the gym"
        )
        self.todo3.done = True
        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )
        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        def mark_done(todo):
            todo.done = True

        self.todos.each(mark_done)
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

    def test_select(self):
        self.todo1.done = True
        selected = self.todos.select(lambda todo: todo.done)
        self.assertEqual("----- Today's Todos -----\n[X] Buy milk",
                     str(selected))


if __name__ == "__main__":
    unittest.main()