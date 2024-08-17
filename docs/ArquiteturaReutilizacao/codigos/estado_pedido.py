from abc import ABC, abstractmethod

class EstadoPedido(ABC):
    @abstractmethod
    def confirmar_pedido(self):
        pass

    @abstractmethod
    def cancelar_pedido(self):
        pass

    @abstractmethod
    def enviar_pedido(self):
        pass
