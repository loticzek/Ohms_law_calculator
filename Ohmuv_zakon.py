#Ohmův zákon
#I=U/R
#U=R*I
#R=U/I
print("Vítej v kalkulačce Ohmova zákona")
print("Pro každou veličinu zadej buď hodnotu a nebo stiskni ENTER")
print("Vždy je třeba zadat dvě veličiny")
print("Pro pokračování stiskni ENTER")
input("")
print("Zadej R")
r = input()
while r == float:
    r = input()
    
else:
    print("chybné zadání")
    break


print("Zadej U")
u = input()
print("Zadej I")
i = input()
if r == "?" or r == "": #zadat otaznik a nebo zmáčknutí ENTER
    napeti = float(u)
    proud = float(i)
    vysledek = napeti / proud
    print("vysledek je", vysledek, "ohm")
if u == "?" or u == "": #zadat otaznik a nebo zmáčknutí ENTER
    odpor = float(r)
    proud = float(i)
    vysledek = odpor * proud
    print("vysledek je", vysledek, "V")
if i == "?" or i == "": #zadat otaznik a nebo zmáčknutí ENTER
    napeti = float(u)
    odpor = float(r)
    vysledek = napeti / odpor
    print("vysledek je", vysledek, "A")
if r != "" and i != "" and u != "":
    print("nelze spočítat")




