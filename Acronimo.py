
#Acronimo

Phrase = input("Insert your phrase: ")
Phrase1 = Phrase.split()
Letters = Phrase[0].upper()

for i in range(1, len(Phrase)):
    if Phrase[i] == " ":
        Letters += Phrase[i+1].upper()

print(Letters)