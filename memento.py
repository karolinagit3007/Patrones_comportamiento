class TextMemento:
    def __init__(self, text):
        self.text = text

class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return TextMemento(self.text)
    
    def restore(self, memento):
        self.text = memento.text

    def show(self):
        print(f"Contenido actual: {self.text}")

class History:
    def __init__(self):
        self.mementos = []

    def add(self, memento):
        self.mementos.append(memento)

    def undo(self):
        if len(self.mementos) > 0:
            return self.mementos.pop()
        return None
    
editor = TextEditor()
history = History()

editor.write("Hola, ")
history.add(editor.save())

editor.write("mundo!")
history.add(editor.save())

editor.show()

memento = history.undo()
editor.restore(memento)
editor.show()
