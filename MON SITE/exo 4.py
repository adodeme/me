
"""age=int(input("Quelle est ton âge? :"))
if 0<age<6
   print("Yo, tu peux être mon enfant, toi!") 
elif age==6 or age==7:
    print("Yo bro, tu es un poussin")
elif age==8 or age==9:
    print("Yo bro, tu es une pupille")
elif age==10 or age==11:
    print("Yo bro, tu es un minime")
elif 12<=age<=18:
    print("Yo bro, tu es un cadet")
else:
    print("Yo,t'es pas un rnfant, toi!")"""










"""a=float(input("Entrez la valeur de a! \n a="))
b=float(input("Entrez la valeur de b! \n b="))
print("On a donc:",a*"x","+",b,"=0")
print("La solution de cette equation est : \n x=",-b/a)"""









"""a=float(input("Entrez le premier nombre"))
b=float(input("Entrez le second nombre"))
if a*b<0:
    print("Le produit axb est négatif")
else:
    print("Le produit axb est positif")









n1=int(input("Quel est le nombre de doigt de A ?"))
n2=int(input("Quel est le nombre de doigt de B ?"))
z=A+B 
if z%2=0:
    print("Celui qui remporte cette partie est le joueur A. Bravo à vous !!!")
elif z%2=1:
    print("Celui qui remporte cette partie est le joueur B. Bravo à vous !!!")
else :
    print("Jeu nul !!!")"""












n1=int(input("Quel est le nombre de doigt de A ?"))
while 0>n1 or n1>5 :
    n1=int(input("Erreur: veuillez réessayer !\n Quel est le nombre de doigt de A ? "))


n2=int(input("Quel est le nombre de doigt de B ?"))
while 0>n1 or n1>5 :
    n1=int(input("Erreur: veuillez réessayer !\n Quel est le nombre de doigt de B ? "))

z=n1+n2 
if  z%2==0 :
    print("Celui qui remporte cette partie est le joueur A. Bravo à vous !!!")
elif z%2==1:
    print("Celui qui remporte cette partie est le joueur B. Bravo à vous !!!")
else :
    print("Jeu nul !!!")









"""0
while n1<=0 :
    n1=int(input("Quel est le nombre de doigt de A ?"))
    print("Erreur: veuillez réessayer !")"""







import random
x=random.randint(0,100)
print("Welcom in this program. You are invited to guess a nomber between 1 and 100. Good luck !!!") 
    for i in range(6):
         nb=int(input("Enter you nomber :"))
         if nb>x:
         print("trop élevé :le nombre à trouver est inférieur à ce nombre.Nouvelle chance !")
        elif nb<x :
        print("Trop faible :le nombre à trouver est supérieur à ce nombre.Nouvelle chance !")
        elif nb==x:
        print("Bien joué. Vous avez trouvé le nombre secret !!!")
     
















 nb=0
while nb<>0:   
 nb=int(input("Enter you nomber :"))
    if nb>x:
         print("trop élevé :le nombre à trouver est inférieur à ce nombre.Nouvelle chance !")
    elif nb<x :
        print("Trop faible :le nombre à trouver est supérieur à ce nombre.Nouvelle chance !")
    else: 
        print("Bien joué. Vous avez trouvé le nombre secret !!!")















import random
x=random.randint(0,100)
print("Welcom in this program. You are invited to guess a nomber between 1 and 100. Good luck !!!") 
for i in range(6):
     nb=int(input("Enter you nomber :"))
     if nb>x:
         print("trop élevé :le nombre à trouver est inférieur à ce nombre.Nouvelle chance !")
     elif nb<x :
        print("Trop faible :le nombre à trouver est supérieur à ce nombre.Nouvelle chance !")
    else: 
        print("Bien joué. Vous avez trouvé le nombre secret !!!")























