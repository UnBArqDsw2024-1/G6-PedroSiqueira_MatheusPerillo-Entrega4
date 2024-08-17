from estados_concretos import AguardandoPagamento, PagamentoAprovado, EmSeparacao
from pedido import Pedido
from pagamento_factory import PIXFactory, BoletoFactory, CartaoCreditoFactory
from produto_concreto import Produto
from produto_decorators import ProdutoComDesconto, ProdutoEmbalagemPresente

def main():
    produto = Produto("Camiseta", 50.0)
    
    produto_com_desconto = ProdutoComDesconto(produto, 0.10)  
    produto_final = ProdutoEmbalagemPresente(produto_com_desconto)

    print("Descrição do Produto:", produto_final.get_descricao())
    print("Preço Final do Produto:", produto_final.get_preco())

    pedido = Pedido(AguardandoPagamento())

    pedido.confirmar_pedido()  
    pedido.enviar_pedido()     

    pedido.set_estado(PagamentoAprovado())
    pedido.enviar_pedido()      

    pagamento_factory = CartaoCreditoFactory()
    pagamento = pagamento_factory.criar_pagamento()
    pagamento.realizar_pagamento(produto_final.get_preco())

    pedido.set_estado(EmSeparacao())
    pedido.enviar_pedido()      

if __name__ == "__main__":
    main()
