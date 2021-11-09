 

def square_of_sum(num1, num2):

    tot = 0

    for x in range(1, 2+1):

        tot = tot+x

    print('The Square of the Sum',tot*tot)

    return tot*tot

def sum_of_square(num1, num2):

    tot = 0

    for x in range(num1, num2+1):

       tot = tot+(x*x)

print('The Sum of the Square ',tot )

return tot

#Ask the user  for his input.
num1 = int(input('Enter First number in the range: '))
num2 = int(input('Enter the last number in the range: '))

#Call the functions.
w1 = square_of_sum(num1 ,num2)
w2 = sum_of_square(num1, num2)

#Output the Difference.

print("the Difference is: ", w1-w2)
