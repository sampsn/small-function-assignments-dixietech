def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    return multiply(x, x)

def add_squares(x: float, y: float) -> float:
    return add(square(x), square(y))


def main():
    print(add(5, 10))
    print(multiply(2, 5))
    print(square(12))
    print(add_squares(12, 4))

if __name__ == "__main__":
    main()
