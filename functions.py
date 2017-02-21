def function_one():
    print("One!")

def function_two():
    print("Two!")

def function_three():
    print("Three!")

function_list = [function_one, function_two, function_three]

if __name__ == '__main__':
    for func in function_list:
        print(func.__name__)
        func()

