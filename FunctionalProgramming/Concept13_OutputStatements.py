print("Hello\nDharani")  # we can pass escape characters to print function
print()  # just prints a new line character
print("Good\tMorning")
print("Dharani" * 3)  # we can use repetition operator like this in print function

print("Dharani" + "Kumar")  # the output doesn't have any space
print("Dharani", "Kumar")  # the output will have space

# by default if we pass multiple arguments to print function they are separated by space

a, b, c = 10, 20, 30
print("The values of the variables are : ", a, b, c)  # we can pass any number of arguments to print function
print(a, b, c, sep=',')  # sep can be used to pass our own delimiter to print function

print("Hello", end=' ')  # by default print will add \n at the end of the string
print("Team", end=' ')  # we can change this behaviour by using the 'end' like this
print("Python is very easy")

print(10, 20, 30, 40, sep=':', end='...')
print(50, 60, 70, 80, sep='-')
