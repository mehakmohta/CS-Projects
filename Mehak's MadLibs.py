import random

playtime = int(input("How many times would you like to play? (Up to 3) allowed"))

while playtime>3:
    print("Sorry. Try again")
    int(input("Enter the number of times you would like to play (must be less than three"))


count = 0

while count<=playtime:
    noun = input("Enter a noun")
    verb = input("Enter a verb")
    adjective = input("Enter an adjective")

    sentences = [f"My pet {noun} loves to {verb} on the {adjective} furniture",
             f"We danced with a {adjective} {noun} last night",
             f"The {adjective} cat {verb}ed over the {noun}"]

    currentsentence = random.choice(sentences)
    
    print(currentsentence)
    count+=1
    
print(Finished!)



