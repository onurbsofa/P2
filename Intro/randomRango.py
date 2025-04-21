#generador de numeros random
# genera una lista inmodificable de numeros en orden creciente
# - tiene en cuenta los anteriores elegidos que se alamcenan en un set que es una estructura de datos inmodificable
# - no se pueden repetir
import random

def generate_unique_random_numbers(start, end, count):
    """
    Generates a list of unique random numbers within a specified range.
    
    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.
    count (int): The number of unique random numbers to generate.
    
    Returns:
    list: A list of unique random numbers.
    """
    if count > (end - start + 1):
        raise ValueError("Count is larger than the range of unique numbers available.")
    
    random_numbers = set()
    while len(random_numbers) < count:
        number = random.randint(start, end)
        random_numbers.add(number)
    
    return list(random_numbers)

# Example usage
start_range = 1
end_range = 204
number_count = 134

random_numbers = generate_unique_random_numbers(start_range, end_range, number_count)
print("Generated unique random numbers:", random_numbers)