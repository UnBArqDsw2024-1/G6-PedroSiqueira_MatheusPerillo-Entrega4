from produto_interface import ProdutoInterface

class ProdutoDecorator(ProdutoInterface):
    def __init__(self, produto: ProdutoInterface):
        self._produto = produto

    def get_descricao(self) -> str:
        return self._produto.get_descricao()

    def get_preco(self) -> float:
        return self._produto.get_preco()

class ProdutoComDesconto(ProdutoDecorator):
    def __init__(self, produto: ProdutoInterface, desconto: float):
        super().__init__(produto)
        self.desconto = desconto

    def get_preco(self) -> float:
        preco_base = super().get_preco()
        return preco_base - (preco_base * self.desconto)

class ProdutoEmbalagemPresente(ProdutoDecorator):
    def get_descricao(self) -> str:
        return super().get_descricao() + " com embalagem para presente"

    def get_preco(self) -> float:
        return super().get_preco() + 5.0
