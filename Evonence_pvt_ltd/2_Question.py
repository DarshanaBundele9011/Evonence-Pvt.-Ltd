import time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)
        end_time = time.time()   
        execution_time = end_time - start_time
        print(f"⏱ Function '{func._name_}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
result = calculate_sum(1000000)
print("Result:", result)