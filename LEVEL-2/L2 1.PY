nums = [4,54,29,71,59,98,23]
prime = comp = 0
for n in nums:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                comp += 1
                break
        else:
            prime += 1
print("composite numbers=", comp)
print("prime numbers=", prime)
