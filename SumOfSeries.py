# Sum of Series = 1 + x^2/2 + x^3/3 + … x^n/n

# Taking input from the user.
n=int(input("Enter the number of terms:"))

# Taking input from the user.
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
print("The sum of series is",round(sum1,2))

# 1 + x^2/2 + x^3/3 + … x^n/n
