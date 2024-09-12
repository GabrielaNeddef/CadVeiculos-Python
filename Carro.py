from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas):
        super().__init__(marca, modelo, placa,ano)
        self.__n_portas = n_portas

    def __str__(self):
        retorno = super().__str__()
        return f'''{retorno}
-cilindradas:{self.__n_portas}'''
