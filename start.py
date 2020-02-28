def main():
    pass

# łańcuchy znaków
imie = "Gabriel"
print(imie)
print(type(imie))
print(type(5))
print(type(5.7))
print(type(True))
print(type(None))

print(imie[2])
#imie[0] = "G"
imie = "Damian"
imie = imie.lower()
print(imie)
wiek = 30
#print(imie + " ma " + wiek + " lat.") 
print(imie + " ma " + wiek.__str__() + " lat.") 
print(imie + " ma " + str(wiek) + " lat.") 
print("{} ma {} lat.".format(imie, wiek)) 
print("{0} ma {1} lat.".format(imie, wiek)) 
# f-string
print(f"{imie} ma {wiek} lat.") 
# pyformat.info
liczba = 6.78654322134
print(f"{liczba:.2f}")

# typ liczbowy
liczba = 5
liczbaf = 5.5
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2) # zielenie bez reszty
print(1 ** 2) # potęgowanie
print(1 % 2) # modulo

tekst = "100"
liczba_z_tekstu = int(tekst, 8)
print(liczba_z_tekstu)
import math
pi = 3.15
from math import *
from math import pow , sqrt, pi
import math as m
m.pow(2, 2)
print(m.pi)

# listy
lista = [] #pusta
lista2 = list() #pusta
lista3 = [1, 2, 3] 
lista3 = [1, "ALa", True, None, [1, 2,]] 
lista3[1] = "Zosia"
#lista5[1][0] = "O"
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print (macierz[1][1])
print(0.1 + 0.2 == 0.3)
# Decimal
print(f"{0.1:.32f}")

lista = lista + lista3
lista += lista3

# Słownik
slownik = {}
slownik = dict()
slownik3 = {"klucz": "wartość"}
slownik3['klucz'] = 100
slownik3[0] = 999
print(slownik3)
slownik3.keys()
slownik3.values()
print(slownik3.items())




