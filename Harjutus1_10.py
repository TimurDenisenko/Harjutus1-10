from math import *
from re import A
from random import *

#1
print("1 harjutus")
C=float(input("Puu ümbermõõt - "))
d=round(C/pi,2)
print("Puu läbimõõt - ", d)

#2
print("")
print("2 harjutus")
N=float(input("Ristküliku pikkus - "))
M=float(input("Ristküliku laius - "))
dr=sqrt(N**2 + M**2)
print(f"Ristkülik diagonaal - {dr}")

#3
print("")
print("3 harjutus")
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu km sõitsid? "))
kiirus = teepikkus / aeg #Viga oli kiiruse valemis

print("Sinu kiirus oli " + str(kiirus) + " km/h")
print("Viga oli kiiruse valemis")

#4
print("")
print("4 harjutus")
ea=int(input("Esimene number - "))
ta=int(input("Teine number - "))
ka=int(input("Kolmandaks number - "))
na=int(input("Neljas number - "))
va=int(input("Viies number - "))
sr=float((ea + ta + ka + na + va) / 5)
print(f"Keskmine - {sr}")

#5
print("")
print("5 harjutus")
print('  @..@\n (----)\n (\__/)\n^^ "" ^^')

#6
print("")
print("6 harjutus")
a=int(input("Kolmnurga 1 külg - "))
b=int(input("Kolmnurga 2 külg - "))
c=int(input("Kolmnurga 3 külg - "))
P= a + b + c
print(f"Kolmnurga ümbermõõt - {P}")

#6.5
print("")
print("6.5 harjutus (random)")
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a},\nb={b},\nc={c}.")
P= a + b + c
print(f"Ümbermõõt on {P}")

#7
print("")
print("7 harjutus")
ia=int(input("Inimeste arv - "))
h=float(input("Pitsa hind - "))
pco=float(input("Jootraha protsent - "))
s=round(((h * pco)/100 + h)/ia,2)
print(f"Pitsa hind - {s}")

#8
print("")
print("8 harjutus")
lt=float(input("Tankimine - "))
pp=float(input("Läbitud vahemaa - "))
k1kk=(lt/pp) * 100
print(f"Kütusekulu 100 km kohta - {k1kk} l")

#9
print("")
print("9 harjutus")
v=float(29.9)
print(f"Rulluisutaja keskmine kiirus on - {v} km/t")
m=v*1000/60
print(f"Keskmine kiirus km/t kuni m/min - {m} m/min")

#10
print("")
print("10 harjutus")
mn=int(input("Sisestage minutite arv - "))
ta=int(mn//60)
ma=mn%60
print(f"{ta}:{ma}")
