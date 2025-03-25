import time
import math

def complex_calculation():
    total = 0
    for i in range(1, 10000):
        total += math.sqrt(i) * math.log(i + 1) / math.sin(i % 180 + 1)
    return total

def benchmark(duration=120):
    start_time = time.time()
    count = 0
    
    while time.time() - start_time < duration:
        complex_calculation()
        count += 1
        print(f"Completed iteration {count}")
    
    elapsed_time = time.time() - start_time
    iterations_per_second = count / elapsed_time
    print(f"Total iterations completed in {duration} seconds: {count}")
    print(f"Iterations per second: {iterations_per_second:.2f}")

if __name__ == "__main__":
    benchmark()
