n = int(input("Enter a number: "))
s = sum(i for i in range(1, n) if n % i == 0)
print("it is a perfect number" if s == n else "it is not a perfect number")
