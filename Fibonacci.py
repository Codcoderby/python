n = int(input("Ne qeder fibonacci ededini yazaq?\n"))
print("Fibonacci ededleri:")
a, b, i, eded = 0, 1, 0, 1
while i < n:
    i += 1
    print(a, end=" ")
    eded = b
    b = b + a
    a = eded
print()
