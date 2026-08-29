# numbers = [10,20,30]

# it = iter(numbers)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("finished")
#         break
    
# numbers = [1,2,3]

# it = iter(numbers)


# print(next(it))

# for x in it:
#     print(x)

# def numbers():
#     return[1,2,3,4,5]
# result = numbers()
# print(result)

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