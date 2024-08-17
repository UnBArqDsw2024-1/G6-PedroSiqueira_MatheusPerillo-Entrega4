from produto_concreto import Produto
from produto_decorators import ProdutoComDesconto, ProdutoEmbalagemPresente

def main():
    produto = Produto("Camiseta", 50.0)
    produto_com_desconto = ProdutoComDesconto(produto, 0.10)  
    produto_com_embalagem = ProdutoEmbalagemPresente(produto_com_desconto)

    print(produto_com_embalagem.get_descricao())  
    print(produto_com_embalagem.get_preco())  

if __name__ == "__main__":
    main()
