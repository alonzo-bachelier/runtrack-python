for number in range(0, 101):
 
    fizz = not number % 3
    buzz = not number % 5
 
    if fizz and buzz :
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(number)
