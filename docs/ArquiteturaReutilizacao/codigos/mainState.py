from estados_concretos import AguardandoPagamento, PagamentoAprovado, EmSeparacao
from pedido import Pedido

def main():
    pedido = Pedido(AguardandoPagamento())
    pedido.confirmar_pedido()  
    pedido.enviar_pedido()      
    
    pedido.set_estado(PagamentoAprovado())
    pedido.enviar_pedido()      

    pedido.set_estado(EmSeparacao())
    pedido.enviar_pedido()      

if __name__ == "__main__":
    main()
