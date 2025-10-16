a = list(map(int, input("Enter array elements: ").split()))
a.sort()
print(a)
print("Mid-element:", a[len(a)//2])
