from pagamento_interface import PagamentoFactory
from pagamento_concreto import PIX, Boleto, CartaoCredito

class PIXFactory(PagamentoFactory):
    def criar_pagamento(self) -> PIX:
        return PIX()

class BoletoFactory(PagamentoFactory):
    def criar_pagamento(self) -> Boleto:
        return Boleto()

class CartaoCreditoFactory(PagamentoFactory):
    def criar_pagamento(self) -> CartaoCredito:
        return CartaoCredito()
