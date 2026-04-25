#definisco una funzione e la chiamo main
def main():
    #qui dico all'interno della funzione che x  è parte della funzione deve essere intero e deve essere inserito dall'user
    x = int(input("What's x? "))
    #qui devo inventare un'altra funzione is_even e sarà la funzione che mi permetterà di elaborare le condizioni
    #dico di assegnare a is_even il valore di x e di scrivere Even in funzione di una condizione if che abbiamo visto sotto
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#qui andiamo a definire la funzione is_even che fara i confronti e diciamo che is_even è sicuramente un numero che ancora non conosciamo ma grazie al codice precedente sappiamo che sarà uguale a x
#e gli chiediamo di verificare queste condizioni
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()







