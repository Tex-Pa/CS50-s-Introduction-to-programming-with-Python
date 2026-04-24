#ask user for their name
name = input("What's your name?") .strip().title()
#say hello... questi sono i parametri della funzione in sostanza i parametri sono quelli che si trovano dentro le parentesi
#Il metodo strip serve a ripulire la stringa e ci restituisce il testo togliendo i caratteri invisibili solo all'interno della stringa
#il metodo title ci permette anche esso di pulire la stringa mettendo le maiuscole ad ogni parola
#il metodo .capitalize() mette la maiuscola solo all'inizio della stringa
#il metodo .split() ci permette di dividere il testo in più parti
print("Hello, ", name)
#qui restutuisce due spazi uno spazio arriva dalla stringa e l'altro con l'utilizzo della virgola prima della variabile

