#nominiamo la variabile score e diciamo che deve essere un numero intero e che dovra essere inserita dall'utente
score = int(input("score: "))

if score >= 90 and <= 100 :
    print("Grade: A")
elif score >= 80 and score < 90 :
    print("Grade:B")
elif score >= 70 and < 80:
    print("Grade: C")
elif score >= 60 and < 70 :
    print("Grade: D")
else:
    print("Grade: F")
