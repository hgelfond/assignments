with open('name.txt') as f:
    name = f.read()

print(name)

#writing a text file
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' + name + '.')