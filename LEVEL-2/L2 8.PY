a = list(map(int, input("Enter numbers: ").split()))
if len(a) < 2:
    print("Enter at least 2 numbers")
else:
    a.sort()
    print(a[-2])
