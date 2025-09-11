#Given a string containing an algebraic equation, calculate and return the value of x.(Addition, subtraction))
def evalAlgebra(equation):
    left_side, right_side = equation.split('=')
    result = int(right_side.strip())
    parts = left_side.strip().split()

    if parts[0] == 'x':
        if parts[1] == '+':
            x = result - int(parts[2])
        elif parts[1] == '-':
            x = result + int(parts[2])
    elif parts[2] == 'x':
        if parts[1] == '+':
            x = result - int(parts[0])
        elif parts[1] == '-':
            x = int(parts[0]) - result
    return x

print(evalAlgebra("2 + x = 19"))  
print(evalAlgebra("4 - x = 1"))   