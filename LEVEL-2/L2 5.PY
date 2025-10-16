a = list(map(int, input("Enter array elements: ").split()))
M = int(input("Enter M value: "))
N = int(input("Enter N value: "))
a.sort()
maxM = a[-M]
minN = a[N-1]
print(f"{M}st Maximum Number = {maxM}")
print(f"{N}rd Minimum Number = {minN}")
print("Sum =", maxM + minN)
print("Difference =", maxM - minN)
