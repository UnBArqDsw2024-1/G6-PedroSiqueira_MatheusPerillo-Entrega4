from pagamento_factory import PIXFactory, BoletoFactory, CartaoCreditoFactory

def main():
    boleto_factory = BoletoFactory()
    pagamento_boleto = boleto_factory.criar_pagamento()
    pagamento_boleto.realizar_pagamento(150.0)

    pix_factory = PIXFactory()
    pagamento_pix = pix_factory.criar_pagamento()
    pagamento_pix.realizar_pagamento(200.0)

    cartao_factory = CartaoCreditoFactory()
    pagamento_cartao = cartao_factory.criar_pagamento()
    pagamento_cartao.realizar_pagamento(300.0)

if __name__ == "__main__":
    main()
