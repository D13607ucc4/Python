import random

Number = int(input("Insert a number between 1 and 50: "))

correct2 = False
count = 1

def Iscorrect(Number):
    correct = False
    while not correct:
        if (Number >= 1) and (Number <= 50):
            print("\nYou have inserted the following number:", Number, "\n")
            correct = True
        else:
            print("\nPlease insert a valid number. Try again.\n")
            Number = int(input("Insert a number between 1 and 50: "))

while not correct2:
    Iscorrect(Number)
    Random_number = random.randint(1, 50)
    if Random_number != Number:
        print("The computer has chosen another number: ", Random_number, "\n")
        count += 1
        wantPlay = input("Do you want to continue playing (Y/N): ")
        if wantPlay == 'y':
            Number = int(input("\nInsert a number between 1 and 50: "))
        else:
            print("\nThe game finished\n")
            print("You have played ", count, "times.\n")
            correct2 = True
    else:
        print("\nThe number you chose was the same as the computer.\n")
        print("You have played ", count, "times.")
        correct2 = True