def add(num1, operator, num2):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    

add(3, "-", 3)
add(3, "+", 6)
add(9, "/", 3)
add(9, "*", 3)