# recursivly calling function pow till m==0
def pow(n, m, tmp):
    if (m == 0):
        return tmp
    return pow(n, m-1, tmp*n)


# talking input for num1 and num2
num1 = int(input())
num2 = int(input())

# printing the solutions
print(pow(num1, num2, 1))
