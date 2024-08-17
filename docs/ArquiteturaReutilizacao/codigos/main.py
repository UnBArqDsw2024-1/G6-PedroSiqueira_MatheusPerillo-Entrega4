from estados_concretos import AguardandoPagamento, PagamentoAprovado, EmSeparacao
from pedido import Pedido
from pagamento_factory import PIXFactory, BoletoFactory, CartaoCreditoFactory
from produto_concreto import Produto
from produto_decorators import ProdutoComDesconto, ProdutoEmbalagemPresente

def main():
    # Criando um produto básico
    produto = Produto("Camiseta", 50.0)
    
    # Aplicando um desconto e adicionando embalagem para presente ao produto
    produto_com_desconto = ProdutoComDesconto(produto, 0.10)  # 10% de desconto
    produto_final = ProdutoEmbalagemPresente(produto_com_desconto)

    # Exibindo informações do produto
    print("Descrição do Produto:", produto_final.get_descricao())
    print("Preço Final do Produto:", produto_final.get_preco())

    # Criando um pedido e associando o produto
    pedido = Pedido(AguardandoPagamento())

    # Simulando fluxo do pedido
    pedido.confirmar_pedido()  # Pagamento confirmado
    pedido.enviar_pedido()      # Não é possível enviar ainda, pois pagamento não foi aprovado

    # Mudando estado do pedido para PagamentoAprovado
    pedido.set_estado(PagamentoAprovado())
    pedido.enviar_pedido()      # Pedido enviado para separação

    # Simulando pagamento com uma fábrica (escolhendo Cartão de Crédito como exemplo)
    pagamento_factory = CartaoCreditoFactory()
    pagamento = pagamento_factory.criar_pagamento()
    pagamento.realizar_pagamento(produto_final.get_preco())

    # Mudando estado do pedido para Em Separação
    pedido.set_estado(EmSeparacao())
    pedido.enviar_pedido()      # Pedido enviado para o transporte

if __name__ == "__main__":
    main()
