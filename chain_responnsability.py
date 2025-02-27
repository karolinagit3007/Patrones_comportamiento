from abc import ABC , abstractmethod

class Handler(ABC):
    def init(self, next_handler=None):
        self._next_handler = next_handler

    def set_next(self, next_handler):
        self._next_handler = next_handler
        return next_handler
    
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return
    
class AuthenticationHandler(Handler):
    def handle(self, request):
        if not request.get('authenticated',False):
            return  'Usuario no autenticado'
        print('Autenticacion exitosa')
        return super().handle(request)
    
class AuthorizationHandler(Handler):
    def handle(self, request):
        if not request.get("role")!="admin":
            return 'No tienes permiso para realizar esta accion'
        print('Autorizacion exitosa')
        return super().handle(request)
    
class DataValidationHandler(Handler):
    def handle(self, request):
        if "data" not in request:
            return 'Los datos no son validos'
        print('Validacion de datos exitosa')
        return super().handle(request)
    
authenticationHandler = AuthenticationHandler()
authorizationHandler = AuthorizationHandler()
dataValidationHandler = DataValidationHandler()
authenticationHandler.set_next(authorizationHandler).set_next(dataValidationHandler)

request = {
    'authenticated': True,
    'role': 'admin',
    'data': 'valid'
}

result = authenticationHandler.handle(request)
print(result)
