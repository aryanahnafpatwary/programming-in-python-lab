total=0
for i in range(2, 1000):
    prime=True
    for j in range(2, i):
        if (i % j) == 0:
            prime=False
            break
    if prime:
        total=total+i
print("Total:", total)