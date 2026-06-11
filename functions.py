def load_todos():
    try:
        with open("todo.txt", "r", encoding="utf-8") as f:
            return [
                {
                    "done": line.startswith("[x]"),
                    "text": line[4:].strip()
                }
                for line in f
            ]
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open("todo.txt", "w", encoding="utf-8") as f:
        for t in todos:
            status = "[x]" if t["done"] else "[ ]"
            f.write(f"{status} {t['text']}\n")


def add(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)


def delete(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos.pop(index)
    save_todos(todos)


def edit(index, text):
    todos = load_todos()
    todos[index]["text"] = text
    save_todos(todos)


def toggle(index):
    todos = load_todos()
    todos[index]["done"] = not todos[index]["done"]

    # Done ها برن پایین
    todos.sort(key=lambda x: x["done"])

    save_todos(todos)


def move_up(index):
    todos = load_todos()
    if index > 0:
        todos[index], todos[index - 1] = todos[index - 1], todos[index]
    save_todos(todos)


def move_down(index):
    todos = load_todos()
    if index < len(todos) - 1:
        todos[index], todos[index + 1] = todos[index + 1], todos[index]
    save_todos(todos)