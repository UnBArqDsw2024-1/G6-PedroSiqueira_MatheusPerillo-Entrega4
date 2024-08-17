from abc import ABC, abstractmethod

class ProdutoInterface(ABC):
    @abstractmethod
    def get_descricao(self) -> str:
        pass

    @abstractmethod
    def get_preco(self) -> float:
        pass
