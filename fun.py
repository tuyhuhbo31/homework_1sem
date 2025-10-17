with open('new.txt', 'r') as file:
    text = file.read()
print(sum(1 for char in text if char in '.!?'))


