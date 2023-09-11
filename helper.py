from dataclasses import dataclass
import datetime
import operator

todos = []


@dataclass
class Todo:
    title: str
    date: datetime = "01/01/23"
    isCompleted: bool = False


def add(title, date):
    title = title.replace("b", "bbb").replace("B", "Bbb")  # Ver-BBB-isierung
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    todos.append(Todo(title, date))  # Daten speichern

    todos.sort(key=operator.attrgetter("date"))  # Liste sortieren, LA1620


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def delete_all():
    todos.clear()
