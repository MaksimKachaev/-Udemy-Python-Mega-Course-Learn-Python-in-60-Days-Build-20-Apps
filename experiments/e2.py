#elem = ['tails', 'heads', 'tails', 'tails', 'heads']

mas = []
tailsCounter = 0

with open('../files/headsOrTails.txt', 'r') as file:
    a = file.readlines()
    tailsCounter = a.count('tails')
    print(tailsCounter)
    file.close()


