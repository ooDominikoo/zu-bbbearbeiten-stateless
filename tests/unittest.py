import unittest, helper

class TestTodo(unittest.TestCase):

    #hinzufügen
    def test_add(self):
        helper.delete_all()
        helper.add("unittest")
        self.assertEqual(helper.todos[0].title, "unittest")
        self.assertEqual(helper.todos[0].isCompleted, False)

    #updaten
    def test_update(self):
        helper.update(0)
        self.assertTrue(helper.todos[0].isCompleted)

    #verbbbisierung
    def test_verbbbisierung(self):
        titel = "b"
        helper.add(titel)
        item = helper.todos[1].title
        self.assertEqual(item, "bbb")

        titel2 = "B"
        helper.add(titel2)
        item2 = helper.todos[2].title
        self.assertEqual(item2, "Bbb")

        


# zum starten
# py -m unittest tests/unittest.py