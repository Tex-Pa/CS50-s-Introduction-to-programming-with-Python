#int sono i numeri interi
#supportano gli operatori + - * / %
#il simbolo % ci restituisce il resto di una divisione

#qui nominiamo la variabile che verrà inserita dall'operatore sia x che y
x = input("what's x? ")
y = input("what's y? ")

#qui diciamo al traduttore che le due nostre variabili sono numeri interi per non farle considerare come stringhe
z = int(x) + int(y) 

#qui chiediamo di mostrare il risultato a video
print(z)