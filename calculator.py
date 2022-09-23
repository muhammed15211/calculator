#CALC

#ADD
def add(n1, n2):
    return n1 + n2

#MINUS
def minus(n1, n2):
    return n1 - n2

#DIVISION
def division(n1, n2):
    return n1/n2

#MULTIPLY
def multiply(n1, n2):
    return n1 * n2

operations = {
        "+": add,
        "-": minus,
        "/": division,
        "*": multiply,
    }

def calc():
    num = float(input("What's the first number? "))
    for signs in operations:
        print(signs)

    end = True
    while end:
        operation_signs = input("Pick a sign from above: ")
        next_number = float(input("What's the next number? "))
        function = operations[operation_signs]
        answer = function(num, next_number)
        print(f"{num} {operation_signs} {next_number} = {answer}")

        stop = input("Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.:  ").lower()
        if stop == 'y':
            num = answer
        else:
            if stop == 'n':
                calc()
            end = False

calc()
        





