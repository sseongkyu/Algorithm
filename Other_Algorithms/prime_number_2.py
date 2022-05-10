# prime_number_약수
import math

# prime_number discrimination function


def is_prime_number(x):
    # check all value from 2 to x^2
    for i in range(2, int(math.sqrt(x))+1):
        # if x is divisible by that value
        if x % i == 0:
            return False  # Not prime_number
    return True  # prime_number


print(is_prime_number(4))
print(is_prime_number(7))
