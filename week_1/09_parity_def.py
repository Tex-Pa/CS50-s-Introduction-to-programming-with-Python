#definisco una funzione e la chiamo main
def main():
    #qui dico all'interno della funzione che x che è parte della funzione deve essere intero e deve essere inserito dall'user
    x = int(input("What's x? "))
    #qui devo inventare un'altra funzione is_even e sarà la funzione che mi permetterà di di elaborare le condizioni
    #qui l'unica cosa che non capisco è la x tra le parentesi
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#qui andiamo a definire la funzione is_even che fara i confronti ma ancora non capisco cosa significa la n tra parentesi, cosa indica e perchè si mette
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
    main()







