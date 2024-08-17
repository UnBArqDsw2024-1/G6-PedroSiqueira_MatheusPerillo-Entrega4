from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor: float):
        pass

class PagamentoFactory(ABC):
    @abstractmethod
    def criar_pagamento(self) -> Pagamento:
        pass
