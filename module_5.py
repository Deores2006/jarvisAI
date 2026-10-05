numbers = [10,20,30]

it = iter(numbers)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("finished")
        break
    
numbers = [1,2,3]

it = iter(numbers)


print(next(it))

for x in it:
    print(x)

def numbers():
    return[1,2,3,4,5]
result = numbers()
print(result)

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

result = numbers()
print(next(result))
print(next(result))
print(next(result))

list_1 = ["saurabh","sahadev","python"]
list_2 = ["sarthak","ML"]

x = zip(list_1,list_2)
print(list(x))

def numbers():
    return [1,2,3,4,5]

result = numbers()
print(result)

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

result = numbers()
print(next(result))
print(next(result))
print(next(result))
print(next(result))

def test():
    return 10
    return 20

result = test()
print(result)

def demo():
    print("start")
    yield 10
    print("middle")
    yield 20
    print("End")

g = demo()
print(next(g))
print(next(g))

def numbers():
    for i in range(1,6):
        yield i

g = numbers()

for x in g:
    print(x)

def squares(n):
    for i in range(n):
        yield i*i

for x in squares(5):
    print(x)

def numbers():
    for i in range (1,4):
        yield i

g = numbers()

for x in g:
    print(x)

print("Again:")

for x in g:
    print(x)

def even_numbers():
    for i in range(1,11):
        if i%2 == 0:#             yield i

g = even_numbers()

print(next(g))
print(next(g))

for x in g:
    print(x)

g = (x*x for x in range(1,6))

print(next(g))
print(next(g))

print(list(g))

def read_data():
    for i in range(1,6):
        print("reading data:")
        yield i * 10

data = read_data()

print(next(data))
print(next(data))
