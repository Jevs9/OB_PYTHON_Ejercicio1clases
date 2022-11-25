class Vehiculo:
    color = "verde"
    ruedas = 4
    puertas = 5
class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 2200
coche1 = Coche
print(f'Coche1 -- Color: {coche1.color}| ruedas: {coche1.ruedas}| puertas: {coche1.puertas}| velocidad: {coche1.velocidad}| cilindrada: {coche1.cilindrada}')