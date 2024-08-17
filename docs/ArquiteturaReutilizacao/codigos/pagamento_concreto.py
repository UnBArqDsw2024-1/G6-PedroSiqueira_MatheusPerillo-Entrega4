from pagamento_interface import Pagamento

class PIX(Pagamento):
    def realizar_pagamento(self, valor: float):
        print(f"Pagamento de R$ {valor} realizado via PIX.")

class Boleto(Pagamento):
    def realizar_pagamento(self, valor: float):
        print(f"Pagamento de R$ {valor} realizado via Boleto.")

class CartaoCredito(Pagamento):
    def realizar_pagamento(self, valor: float):
        print(f"Pagamento de R$ {valor} realizado via Cartão de Crédito.")
