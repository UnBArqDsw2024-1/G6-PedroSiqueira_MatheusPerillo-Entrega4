from produto_interface import ProdutoInterface

class Produto(ProdutoInterface):
    def __init__(self, descricao: str, preco: float):
        self.descricao = descricao
        self.preco = preco

    def get_descricao(self) -> str:
        return self.descricao

    def get_preco(self) -> float:
        return self.preco
