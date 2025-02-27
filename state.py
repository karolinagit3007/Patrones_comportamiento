from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_money(self):
        pass

    @abstractmethod
    def select_product(self):
        pass

    @abstractmethod
    def dispense(self):
        pass

class NoMoneyState(State):
    def insert_money(self):
        print("Dinero insertado")
        return HasMoneyState()

    def select_product(self):
        print("No puedes comprar nada sin dinero")
        return self
    
    def dispense(self):
        print("No puedes dispensar, no hay dinero")
        return self
    
class HasMoneyState(State):
    def insert_money(self):
        print("Ya hay dinero insertado.")
        return self
    
    def select_product(self):
        print("Producto seleccionado")
        return DispensedState()
    
    def dispense(self):
        print("Debes seleccionar un producto")
        return self
    
class DispensedState(State):
    def insert_money(self):
        print("No puedes insertar dinero después de dispensar")
        return self
    
    def select_product(self):
        print("No puedes seleccionar un producto ya lo has seleccionado")
        return self
    
    def dispense(self):
        print("Producto dispensado")
        return NoMoneyState()

class VendingMachine:
    def __init__(self):
        self.state = NoMoneyState()

    def insert_money(self):
        self.state = self.state.insert_money()
    
    def select_product(self):
        self.state = self.state.select_product()
    
    def dispense(self):
        self.state = self.state.dispense()

machine = VendingMachine()

machine.select_product()
machine.insert_money()
machine.dispense()
machine.select_product()
machine.insert_money()
machine.dispense()
