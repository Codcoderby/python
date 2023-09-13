def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
def find_prime_numbers(start, end):
    prime_numbers = []
    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers
print("@codcoder_project")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_numbers = find_prime_numbers(start, end)
print(f"Prime numbers between {start} and {end}: {prime_numbers}")