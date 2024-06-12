# Functions with multiple parameter
def greet(name):
    print(f"Hello, {name}.")


def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What it is like in {location}?")


def find_maximum(*args):
    maximum = args[0]
    for arg in args:
        if maximum < arg:
            maximum = arg
    return maximum


greet("Priom")
greet_with("Priom", "Cumilla")
print(find_maximum(10, 20, 15))

