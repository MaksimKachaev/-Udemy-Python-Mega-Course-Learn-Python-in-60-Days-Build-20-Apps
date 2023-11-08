import random
content = []
headsOrTails = ['heads', 'tails']
playerInput = input("Heads or Tails?: ").lower()
computerInput = random.choice(headsOrTails)

while playerInput not in headsOrTails:
    playerInput = input("Try again ").lower()

with open("../files/headsOrTails.txt", 'r') as file:
    content = file.readlines()
    file.close()

    content.append(f"player: {playerInput} || computer: {computerInput}" + '\n')

with open("../files/headsOrTails.txt", 'w') as file:
    file.writelines(content)
    file.close()

with open("../files/headsOrTails.txt", 'r') as f:
    contents = f.read()
    countTails = contents.count("tails")
    countHeads = contents.count("heads")
    percentOfTails = (countTails * 100) / countHeads
    file.close()

if playerInput == computerInput:
    print("Congrats!")
    print(f"You: {playerInput} || Computer: {computerInput}" + '\n')
else:
    print("Loose!")
    print(f"You: {playerInput} || Computer: {computerInput}" + '\n')

print(f"Heads: {countHeads}")
print(f"Tails: {countTails}")
print(f"Percent of tails: {percentOfTails}%")