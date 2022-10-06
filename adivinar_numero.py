import random

#input

print("----------------------------------------------------------")
print("---------------JUGUEMOS-A-ADIVINAR-EL-NUMERO--------------")
print("----------------------------------------------------------")

print("\nHOLA HUMANO,COMENCEMOS A JUGAR")
numero=random.randint(1,100)
intento=0
X=int(input("\nHumano intenta adivinar el numero que elegi: "))

#processing

while  numero!=X:
    intento=intento+1
    if X<numero:
        print("\nCasi humano pero el numero es mas grande\n")
        X=int(input("\nintenta adivinar de nuevo:\n "))

    elif X>numero:
        print("\nCasi humano pero el numero es mas pequeño\n")
        X=int(input("\nintenta adivinar de nuevo:\n "))

    
print("\nWOW humano adivinaste el numero en el" ,intento,"intento\n")