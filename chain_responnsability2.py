from abc import ABC, abstractmethod

class OrderHandler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def set_next(self, next_handler):
        self._next_handler = next_handler
        return next_handler

    @abstractmethod
    def handle(self, order):
        if self._next_handler:
            return self._next_handler.handle(order)
        return "Orden procesada con éxito."

class OrderValidationHandler(OrderHandler):
    def handle(self, order):
        if not order.get("items"):
            return "La orden no tiene artículos."
        print("Orden validada correctamente.")
        return super().handle(order)

class StockCheckHandler(OrderHandler):
    def handle(self, order):
        if not all(item['stock'] > 0 for item in order.get("items", [])):
            return "Uno o más artículos no están en stock."
        print("Stock verificado correctamente.")
        return super().handle(order)

class PaymentHandler(OrderHandler):
    def handle(self, order):
        if not order.get("payment_successful", False):
            return "Pago no realizado correctamente."
        print("Pago procesado correctamente.")
        return super().handle(order)

class ShippingHandler(OrderHandler):
    def handle(self, order):
        if not order.get("address"):
            return "La dirección de envío no está proporcionada."
        print("Envío programado correctamente.")
        return super().handle(order)

order = {
    "items": [{"name": "Laptop", "stock": 10}, {"name": "Mouse", "stock": 5}],
    "payment_successful": True,
    "address": "123 Calle Ficticia, Ciudad"
}

order_validation_handler = OrderValidationHandler()
stock_check_handler = StockCheckHandler()
payment_handler = PaymentHandler()
shipping_handler = ShippingHandler()

order_validation_handler.set_next(stock_check_handler).set_next(payment_handler).set_next(shipping_handler)

result = order_validation_handler.handle(order)

print(result)
