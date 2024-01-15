print("...:::Prosty Kalkulator:::...")

x = int(input("Pierwsza liczba:"))
y = int(input("Druga liczba:"))
z = input("Operator ( +, -, *, /, ** ): ")

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if z == "+":
    print(operators["+"])
elif z == "-":
    print(operators["-"])
elif z == "*":
    print(operators["*"])
elif z == "/":
    print(operators["/"])
elif z == "**":
    print(operators["**"])
else:
    print("Bledny operator!")
