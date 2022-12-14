from decimal import ExtendedContext
from math import *
from re import A
from random import *

#1
print("1 harjutus")
try:
    C=float(input("Puu ümbermõõt - "))
    if C>0:
        d=round(C/pi,2)
        print("Puu läbimõõt - ", d)
    else:
        print("C peab olema suurem kui 0")
except:
    print("Andmetüüp on vale")

#2
print("")
print("2 harjutus")
try:
    N=float(input("Ristküliku pikkus - "))
    M=float(input("Ristküliku laius - "))
    if M>0 and N>0:
        dr=sqrt(N**2 + M**2)
        print(f"Ristkülik diagonaal - {dr}")
    else:
        print("N ja M peab olema suurem kui 0")
except:
    print("M and N peavad olema suurem kui 0")

#3
print("")
print("3 harjutus")
try:
        aeg = float(input("Mitu tundi kulus sõiduks? "))
        teepikkus = float(input("Mitu km sõitsid? "))
        if aeg>0 and teepikkus>=0:
            kiirus = teepikkus / aeg #Viga oli kiiruse valemis

            print("Sinu kiirus oli " + str(kiirus) + " km/h")
            print("Viga oli kiiruse valemis")
        else:
            print("Aeg peab olema suurem kui 0 ja teepikkus peab olema suurem või võrdne kui 0")

except:
    print("Aeg peab olema suurem kui 0 ja teepikkus peab olema suurem või võrdne kui 0")

#4
print("")
print("4 harjutus")
try:
    ea=int(input("Esimene number - "))
    ta=int(input("Teine number - "))
    ka=int(input("Kolmandaks number - "))
    na=int(input("Neljas number - "))
    va=int(input("Viies number - "))
    sr=float((ea + ta + ka + na + va) / 5)
    print(f"Keskmine - {sr}")
except:
    print("Andmetüüp on vale")

#5
print("")
print("5 harjutus")
print('  @..@\n (----)\n (\__/)\n^^ "" ^^')

#6
try:
    print("")
    print("6 harjutus")
    a=int(input("Kolmnurga 1 külg - "))
    b=int(input("Kolmnurga 2 külg - "))
    c=int(input("Kolmnurga 3 külg - "))
    if a>0 and b>0 and c>0:
        P= a + b + c
        print(f"Kolmnurga ümbermõõt - {P}")
    else:
        print(f"Kolmnurga ümbermõõt - {P}")

except:
    print("Kolmnurga külgad peavad olema suurem kui 0")

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
try:
    ia=int(input("Inimeste arv - "))
    h=float(input("Pitsa hind - "))
    pco=float(input("Jootraha protsent - "))
    if ia>0 and h>0 and pco>=0:
        s=round(((h * pco)/100 + h)/ia,2)
        print(f"Pitsa hind - {s}")
    else:
        print("Inimeste arv ja pitsa hind peab olema suurem kui 0 ja jootraha protsent peab olema suurem või võrdne kui 0")

except:
    print("Inimeste arv ja pitsa hind peab olema suurem kui 0 ja jootraha protsent peab olema suurem või võrdne kui 0")

#8
print("")
print("8 harjutus")
try:
    lt=float(input("Tankimine - "))
    pp=float(input("Läbitud vahemaa - "))
    if lt>0 and pp>0:
        k1kk=(lt/pp) * 100  
        print(f"Kütusekulu 100 km kohta - {k1kk} l")
    else:
        print(f"Kütusekulu 100 km kohta - {k1kk} l")

except:
    print("Tankimine ja läbitud vahemaa peavad olema suurem kui 0")

#9
print("")
print("9 harjutus")
try:
    v=float(29.9)
    print(f"Rulluisutaja keskmine kiirus on - {v} km/t")
    m=v*1000/60
    print(f"Keskmine kiirus km/t kuni m/min - {m} m/min")
except:
    print("Andmedtüüp on vale")

#10
print("")
print("10 harjutus")
try:
    mn=int(input("Sisestage minutite arv - "))
    ta=int(mn//60)
    ma=mn%60
    print(f"{ta}:{ma}")
except:
    print("Andmetüüp on vale")

print("")
print("Ema roobot")
hind=int(input("Mis hinded sa koolis saad? "))

if hind==1 :
    print("Ema: Ma tappan sind.")
elif hind==2 :
    print("Ema: Ma ootan et sa parandad see.")
elif hind==3 :
    print("Ema: Mis see on? Palun, õppida hästi!")
elif hind==4 :
    print("Ema: Sa oled tubli poiss!")
elif hind==5 :
    print("Kas sa tahad jäätis või juustuburger?")
elif hind>=6 :
    print("Ärge tehke nalja!")
else:
    print("Errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
