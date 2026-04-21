def calc(a, b, symbol):
    if symbol == "+":
        return a + b
    elif symbol == "-":
        return a - b
    elif symbol == "*":
        return a * b
    elif symbol == "/":
        return a / b
print(calc(3, 6, "+"))