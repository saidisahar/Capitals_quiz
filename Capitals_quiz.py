print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the capital of Tunisia? ")
if answer == "Tunis":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Qatar? ")
if answer == "Doha":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Brazil? ")
if answer == "Brasilia":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Indonesia? ")
if answer == "Jakarta":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")