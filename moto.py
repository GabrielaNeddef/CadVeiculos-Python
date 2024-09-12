from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa,ano)
        self.__cilindradas = cilindradas

    def __str__(self):
        #invoco o metodo __str__() da SUPERCLASSE (veiculo)
        #armazeno o retorno na variavel "retorno"
        retorno = super().__str__()
        #retorno a concatenação do valor da variavel
        #"retorno com as "__cilindradas"
        return f'''{retorno}
-cilindradas:{self.__cilindradas}'''
    

