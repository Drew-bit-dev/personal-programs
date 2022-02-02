print("enter number 1:")
number = int(input())

print("enter number 2:")
number2 = int(input())

print("enter an operation (lowe case x for multiply):")
operation = input()

answer = 0

if(operation == 'x'):
    answer = number * number2
elif(operation == '+'):
    answer = number + number2
elif(operation == '-'):
    answer = number - number2
elif(operation == '/'):
    answer = number / number2
else:
    print("That is not a possible operatin")
    
print(answer)