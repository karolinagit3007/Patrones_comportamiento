from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


    @abstractmethod
    def undo(self):
        pass


class Light:
    def on(self):
        print("Luz encendida")

    def off(self):
        print("Luz apagada")



class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        print("Comando agregado: ", command.__class__.__name__)
        self.commands.append(command)

    def execute_commands(self):
        print("Ejecutando comandos...")
        for command in self.commands:
            command.execute()


    def undo_commands(self):
        if self.commands:
            print("Deshaciendo comandos...")
            self.commands.pop().undo()
        
    def undo_commands(self):
        if self.commands:
            print("Deshaciendo comandos...")
        for command in self.commands:
            command.undo()


remote_control = RemoteControl()


light_on_command = LightOnCommand(Light())
light_of_command = LightOnCommand(Light())

remote_control.add_command(light_on_command)
remote_control.add_command(light_of_command)
remote_control.add_command(light_on_command)


remote_control.execute_commands()
remote_control.undo_commands()

