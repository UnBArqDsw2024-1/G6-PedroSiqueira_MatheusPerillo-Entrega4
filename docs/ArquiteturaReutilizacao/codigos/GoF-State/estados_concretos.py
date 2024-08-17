from estado_pedido import EstadoPedido

class AguardandoPagamento(EstadoPedido):
    def confirmar_pedido(self):
        print("Pagamento confirmado, aguardando aprovação.")

    def cancelar_pedido(self):
        print("Pedido cancelado.")

    def enviar_pedido(self):
        print("Não é possível enviar o pedido. Pagamento ainda não confirmado.")

class PagamentoAprovado(EstadoPedido):
    def confirmar_pedido(self):
        print("Pedido já aprovado.")

    def cancelar_pedido(self):
        print("Pedido cancelado após a aprovação.")

    def enviar_pedido(self):
        print("Pedido enviado para separação.")

class EmSeparacao(EstadoPedido):
    def confirmar_pedido(self):
        print("Pedido já em separação.")

    def cancelar_pedido(self):
        print("Pedido cancelado durante a separação.")

    def enviar_pedido(self):
        print("Pedido enviado para o transporte.")
