def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)