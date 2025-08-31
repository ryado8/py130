def input_generator():
    while True:
        s = input("Enter a string: ")
        if s == "stop":
            break
        yield s

for user_input in input_generator():
    print(user_input)