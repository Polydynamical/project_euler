import math
import tqdm

def is_prime(n: int) -> bool:
    for i in tqdm.tqdm(range(2, round(math.sqrt(n)) + 2)):
        if n % i == 0:
            return False
    return True

print(max([x for x in range(2, round(math.sqrt(600851475144))) if (is_prime(x) and 600851475143 % x == 0)]))
