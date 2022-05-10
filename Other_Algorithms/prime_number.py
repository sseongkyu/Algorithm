# prime_number: basic algorithm
def is_prime_number(x):
    # check all value from 2 to (x-1)
    for i in range(2, x):
        # if x is divisible by that value
        if x % i == 0:
            return False  # not prime_number
    return True  # prime_number


print(is_prime_number(4))
print(is_prime_number(7))
