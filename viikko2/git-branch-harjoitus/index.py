from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") 
print(f"{x} - {y} = {erotus(x, y)}") 
print(f"{x} * {y} = {tulo(x, y)}") 

<<<<<<< HEAD
logger("lopetetaan ohjelma")
print("goodbye!") # muutos
=======
logger("lopetetaan")
print("goodbye!")

# muutos
>>>>>>> 1e2e1bcb71a535169db96725b75437452b27d418
