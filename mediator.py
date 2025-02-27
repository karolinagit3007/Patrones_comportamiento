from abc import ABC

class ChatMediator(ABC):
    pass


class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = [] 

    def add_user(self, user):
        self.users.append(user)

    def send(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)


class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)

    def send(self, message):
        self.mediator.send(message, self)

    def receive(self, message):  
        print(f"{self.name} received: {message}")


chat_room = ChatRoom()
user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)
user3 = User("Charlie", chat_room)

user1.send("Hola!")
user2.send("Cómo estas?")
user3.send("Todo bien, gracias!")
