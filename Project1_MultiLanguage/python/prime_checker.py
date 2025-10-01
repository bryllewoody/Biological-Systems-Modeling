# prime_checker.py
# Program reads numbers from a file and checks if they are prime
from math import isqrt

def is_prime(n):
    if n <= 1:               # 0, 1, and negative numbers are not prime
        return False
    for i in range(2, isqrt(n) + 1):   # Only check divisors up to sqrt(n)
        if n % i == 0:       # If divisible, not prime
            return False
    return True              # Otherwise prime

input_file = "numbers.txt"    # Input file containing numbers
output_file = "results.txt"   # Output file for results

# Read input file contents
with open(input_file, "r") as f:
    content = f.read()

# Replace commas with spaces and split into individual tokens
parts = content.replace(",", " ").split()

numbers = [] # collect numbers from each input
for part in parts:
    try:
        num = float(part)                 # Convert numbers to float
        if num.is_integer():              # Keep only whole numbers
            numbers.append(int(num))
        else:
            print(f"Skipping {part}: not an integer.")
    except ValueError:                    # If not a number at all
        print(f"Skipping {part}: not a number.")

# Check which numbers are prime
results = []
for num in numbers:
    if is_prime(num):
        results.append(f"{num} is a prime number.")
    else:
        results.append(f"{num} is NOT a prime number.")

# Write results to output file
with open(output_file, "w") as f:
    for line in results:
        f.write(line + "\n")

print(f"Processed {len(numbers)} numbers. Results saved to {output_file}")