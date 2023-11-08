filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    a = file.read()
    file.close()
    print(a)
