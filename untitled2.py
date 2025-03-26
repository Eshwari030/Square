#Q1. 
def get_odd_numbers():
    odd_numbers_list = [x for x in range(1, 26) if x % 2 != 0]
    return odd_numbers_lit
#Q2. 
def args_function(*args):
    result = 0
    for num in args:
        result += num
    return result

def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
#Q3.
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iterator = iter(my_list)  # Initializing the iterator

for _ in range(5):
    print(next(my_iterator))  # Iterating and printing


#Q4. 
def count_up_to(n):
    i = 1
    while i <= n:
        yield i  # Yield keyword makes it a generator
        i += 1

# Example usage:
for number in count_up_to(5):
    print(number)
#Q5. 
def primes_less_than(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    for prime in primes:
        yield prime

prime_generator = primes_less_than(1000)

for _ in range(20):
    print(next(prime_generator))
#Q6. 
def fibonacci_first_10():
    a, b = 0, 1
    count = 0
    while count < 10:
        print(a)
        a, b = b, a + b
        count += 1

fibonacci_first_10()
