

def f1(x):
    resultat=0
    resultat=x+9
    return resultat 

         
         
#x,y,c=0
c=0
e=0.001

a= input("Entrer la valeur de a : ")
b= input("Entrer la valeur de b : ")
print("a = ", a)
print("b = ", b)

while f1(a)*f1(b)>0 :
        print("\n Pas de solution dans cet interval")
        print("\nsaisir a nouveau l'interval [a,b] a etudier : ")
        a, b = input("Entrer les valeurs de a et b : ").split()
        print("a = ", a)
        print("b = ", b)

while abs(f1(c)>e) :
    if (f1(a)*f1(c)<0) :
        b=c
    else : 
        if (f1(b)*f1(c)<0) :
            a=c

c=(a+b)/2
print("c = ", c)

 


