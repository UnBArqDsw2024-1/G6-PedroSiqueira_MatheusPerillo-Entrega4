from estado_pedido import EstadoPedido

class Pedido:
    def __init__(self, estado: EstadoPedido):
        self.estado = estado

    def set_estado(self, estado: EstadoPedido):
        self.estado = estado

    def confirmar_pedido(self):
        self.estado.confirmar_pedido()

    def cancelar_pedido(self):
        self.estado.cancelar_pedido()

    def enviar_pedido(self):
        self.estado.enviar_pedido()
