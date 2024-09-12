from moto import Moto
from veiculo import Veiculo

falcon = Moto("Honda", "Falcon NX4", "abc", 2005, 400)

print(falcon.__str__())

cerato = Veiculo("kia", "cerato", "IRL", 2011)

print(cerato.__str__())
