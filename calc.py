print("Hello, You can compare your numbers here!")  # greet the user
name = input("What's your name, first? ")  # ask for name

print("Nice to e-meet you, " + name)  # greet with username
num1 = int(input("Enter the first number, " + name + ": "))
num2 = int(input("Enter the second number: "))

print("PLEASE NOTE: 'add' represents addition, 'sub' represents subtraction, 'mul' represents multiplication and 'div' represents division. When asked for 'TYPE OF OPERATION', mention accordingly!")

# num1 = int(input())
# num2 = int(input())

add = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2


InputByUser = input("TYPE OF OPEARTION: ")


if InputByUser == "add":
    print(add)
elif InputByUser == "sub":
    print(sub)
elif InputByUser == "div":
    print(div)
elif InputByUser == "mul":
    print(mul)
else:
    print("Wrong INput!!!")

# you did it Kunal. you did this program by yourself without any help! Good Work!
